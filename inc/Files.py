from inc import Config

import requests, chalk, re

class FilesCheck:

    def listFolder(self, folder):
        if Config.DEBUG:
            print("[DEBUG] GET : " + folder)
        r = requests.get(folder, verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
        contents = re.findall(r'<td><a href=\".*?\"', r.content.decode('utf-8'))
        for content in contents[1:]:
            content = content[content.find('"')+len('"'):]
            content = content[:content.find("\"")]
            print(chalk.white('\t[+] : ', bold=True) + chalk.yellow(folder + content, bold=True))

    def getFile(self, file):
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.GLPI_URL + file)
        r = requests.get(Config.GLPI_URL + file, verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
        if (r.status_code == 200):
            print(chalk.white('[+] Interesting file found : ', bold=True) + chalk.red(Config.GLPI_URL + file, bold=True))

    def getFolder(self, folder):
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.GLPI_URL + folder)
        r = requests.get(Config.GLPI_URL + folder, verify=False, proxies=Config.PROXY, headers=Config.HEADERS, allow_redirects=False)
        if (r.status_code == 301):
            print(chalk.white('\n[+] Interesting folder found : ', bold=True) + chalk.red(Config.GLPI_URL + folder, bold=True))
            self.listFolder(Config.GLPI_URL + folder)

    def getServer(self, url):
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.SERVER_ROOT + url)
        r = requests.get(Config.SERVER_ROOT + url, verify=False, proxies=Config.PROXY, headers=Config.HEADERS, allow_redirects=False)
        if (r.status_code == 301):
            print(chalk.white('[+] Interesting URL found : ', bold=True) + chalk.red(Config.SERVER_ROOT + url, bold=True))

    def files(self):
        print(chalk.green('\n[+] Performing default files check', bold=True))
        print(chalk.green('==================================\n', bold=True))
        for file in Config.FILES:
            self.getFile(file)
        print(chalk.green('\n[+] Performing default folders check', bold=True))
        print(chalk.green('====================================', bold=True))
        for folder in Config.FOLDERS:
            self.getFolder(folder)
        print(chalk.green('\n[+] Performing default server check', bold=True))
        print(chalk.green('===================================\n', bold=True))
        for url in Config.SERVER:
            self.getServer(url)
