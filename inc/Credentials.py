from inc import Config

import requests, chalk, re

class CredentialsCheck:

    def checkAuthent(self, request, user):
        if request.status_code == 302:
            print(chalk.white('[+] Valid user account found : ', bold=True) + chalk.red(user[0] + ':' + user[1], bold=True))
        elif request.status_code == 200 and request.content.decode('utf-8').find("window.location='/front/") != -1:
            print(chalk.white('[+] Valid user account found : ', bold=True) + chalk.red(user[0] + ':' + user[1], bold=True))

    def getLoginField(self, content):
        firstversion = Config.VERSION.split(".")

        if(int(firstversion[0]) == 0):
            login = "login_name"
        else:
            content = re.findall(r'name="(field[a-z0-9]{14})', content)
            login = content[0]  
        return login


    def getPasswordField(self, content):
        firstversion = Config.VERSION.split(".")

        if(int(firstversion[0]) == 0):
            password = "login_password"
        else:
            content = re.findall(r'name="(field[a-z0-9]{14})', content)
            password = content[1]
        return password

    def getCSRFField(self, content):
        csrf = content[content.find('_glpi_csrf_token" value="')+len('_glpi_csrf_token" value="'):]
        csrf = csrf[:csrf.find('"')]
        return csrf

    def Authenticate(self, user, loginField, passwordField, CSRFField):
        payload = {'_glpi_csrf_token': CSRFField, passwordField: user[1], loginField: user[0], 'submit': 'Submit'}
        cookie = {Config.COOKIE.split('=')[0]:Config.COOKIE.split('=')[1]}
        if Config.DEBUG:
            print("[DEBUG] POST : " + Config.GLPI_URL + "/front/login.php")
        Config.HEADERS['Referer'] = Config.GLPI_URL + "/"
        r = requests.post(Config.GLPI_URL + "/front/login.php", data=payload, cookies=cookie, allow_redirects=False, verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
        self.checkAuthent(r, user)

    def getAuthForm(self, user):
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.GLPI_URL)
        r = requests.get(Config.GLPI_URL, verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
        Config.COOKIE = r.headers.get('Set-Cookie').split(';')[0]
        loginField = self.getLoginField(r.content.decode('utf-8'))
        passwordField = self.getPasswordField(r.content.decode('utf-8'))
        CSRFField = self.getCSRFField(r.content.decode('utf-8'))
        self.Authenticate(user, loginField, passwordField, CSRFField)

    def credentials(self):
        print(chalk.green('\n[+] Performing Credential check', bold=True))
        print(chalk.green('===============================\n', bold=True))
        if Config.CREDSFILE:
            try:
                users = open(Config.CREDSFILE,"r")
                while True:
                    user = users.readline()
                    if not user: 
                        break
                    user = user.rstrip('\n').split(':', 1)
                    if Config.DEBUG:
                        print("[DEBUG] Trying " + user[0] + " : " + user[1])
                    self.getAuthForm(user)
            except Exception as e:
                print(chalk.red('[-] ' + Config.CREDSFILE + ' file not found', bold=True))
                return False

        else:
            for user in Config.USERS:
                if Config.DEBUG:
                    print("[DEBUG] Trying " + user[0] + ":" + user[1])
                self.getAuthForm(user)
