from inc import Config, Exploits, AjaxTelemetry

from urllib.parse import urlparse
from packaging.version import Version
import requests, json, chalk

class UrlCheck:

    def getURLBase(self, content):
        if (content.find("'url_base': '") != -1):
            url_base = content[content.find("'url_base': '")+len("'url_base': '"):]
            url_base = url_base[:url_base.find("'")]
            Config.BASE_URL = url_base
        print(chalk.white('[+] url_base : ', bold=True) + chalk.yellow(Config.BASE_URL, bold=True))

    def getRootDoc(self, content):
        if (content.find("'root_doc': '") != -1):
            root_doc = content[content.find("'root_doc': '")+len("'root_doc': '"):]
            root_doc = root_doc[:root_doc.find("'")]
            Config.ROOT_DOC = root_doc
        print(chalk.white('[+] root_doc : ', bold=True) + chalk.yellow(Config.ROOT_DOC, bold=True))

    def tryTelemetry(self):
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.BASE_URL + "/ajax/telemetry.php")
        r = requests.get(Config.BASE_URL + "/ajax/telemetry.php", verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
        if (r.status_code == 200):
            content = r.content.decode('utf-8')
            Config.AJAX_TELEMETRY = json.loads(content[content.find('{'):content.find('</code></pre>')])

    def getVersion(self, request):
            try:
                version = request.content[request.content.find('GLPI version ')+len('GLPI version '):]
                version = version[:version.find(' Copyright')]
                Version(version)
                return version
            except:
                pass
            try:
                version = request.content[request.content.find('?v=')+len('?v='):]
                version = version[:version.find('"')]
                Version(version)
                return version
            except:
                pass
            try:
                version = request.content[request.content.find('">GLPI ')+len('">GLPI '):]
                version = version[:version.find(' Copyright')]
                Version(version)
                return version
            except:
                return False

    def checkVersion(self):
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.BASE_URL)
        if not Config.VERSION:
            if not AjaxTelemetry().getGLPIVersion():
                r = requests.get(Config.BASE_URL, verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
                Config.VERSION = self.getVersion(r.decode('utf-8'))
            if not Config.VERSION:
                print(chalk.white('[!] Cannot find GLPI Version', bold=True))
                return False
        print(chalk.white('[+] Version of GLPI : ', bold=True) + chalk.yellow(Config.VERSION, bold=True))
        Exploits().verifExploit('GLPI', Config.VERSION)
    
    def checkServer(self):
        # try:
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.BASE_URL)
        r = requests.get(Config.BASE_URL, timeout=10, verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
        print(chalk.white('[+] Server Header : ', bold=True) + chalk.yellow(r.headers['Server'], bold=True))
        self.getURLBase(r.content.decode('utf-8'))
        self.getRootDoc(r.content.decode('utf-8'))
        self.tryTelemetry()
        self.checkVersion()
        return True
        # except Exception as e:
        #     print(chalk.red('[-] ' + Config.BASE_URL + ' seems not accessible', bold=True))
        #     return False

    def getInfo(self):
        print(chalk.green('[+] Gathering basic information', bold=True))
        print(chalk.green('===============================\n', bold=True))
        if (self.checkServer()):
            return True
        return False
