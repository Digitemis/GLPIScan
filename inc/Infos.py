from inc import Config, Exploits, AjaxTelemetry

from urllib.parse import urlparse
from packaging.version import Version
import requests, json, chalk

class UrlCheck:

    def tryTelemetry(self):
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.GLPI_URL + "/ajax/telemetry.php")
        r = requests.get(Config.GLPI_URL + "/ajax/telemetry.php", verify=False, proxies=Config.PROXY, headers=Config.HEADERS)

        if (r.status_code == 200):
            try:
                content = r.content.decode('utf-8')
                Config.AJAX_TELEMETRY = json.loads(content[content.find('{'):content.find('</code></pre>')])
            except:
                return False


    def tryGetVersion(self):
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.GLPI_URL + "/ajax/telemetry.php")
        r = requests.get(Config.GLPI_URL + "/ajax/telemetry.php", verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
        if (r.status_code == 200):
            content = r.content.decode('utf-8')
            Config.AJAX_TELEMETRY = json.loads(content[content.find('{'):content.find('</code></pre>')])

    def getVersion(self, content):
            try:
                version = content[content.find('GLPI version ')+len('GLPI version '):]
                version = version[:version.find(' Copyright')]
                Version(version)
                return version
            except:
                pass
            try:
                version = content[content.find('?v=')+len('?v='):]
                version = version[:version.find('"')]
                Version(version)
                return version
            except:
                pass
            try:
                version = content[content.find('">GLPI ')+len('">GLPI '):]
                version = version[:version.find(' Copyright')]
                Version(version)
                return version
            except:
                pass
            try:
                # Find GLPI version V10.XX.XX
                r = requests.get(Config.GLPI_URL + "/public/lib/photoswipe.js.map", verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
                if (r.status_code == 200):
                    content = r.content.decode('utf-8')

                    first_index = content.find('glpi-')
                    second_index = content.find('/glpi/node_modules/', first_index)
                    version = content[first_index+5:second_index]
                    return version
            except:
                return False

    def checkVersion(self):
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.GLPI_URL)
        if not Config.VERSION:
            if not AjaxTelemetry().getGLPIVersion():
                r = requests.get(Config.GLPI_URL, verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
                Config.VERSION = self.getVersion(r.content.decode('utf-8')).strip()
            if not Config.VERSION:
                print(chalk.white('[!] Cannot find GLPI Version', bold=True))
                return False
        print(chalk.white('[+] Version of GLPI : ', bold=True) + chalk.yellow(Config.VERSION, bold=True))
        Exploits().verifExploit('GLPI', Config.VERSION)
    
    def checkServer(self):
        try:
            if Config.DEBUG:
                print("[DEBUG] GET : " + Config.GLPI_URL)
            r = requests.get(Config.GLPI_URL, timeout=10, verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
            print(chalk.white('[+] Server Header : ', bold=True) + chalk.yellow(r.headers['Server'], bold=True))
            Config.SERVER_ROOT = "/".join(Config.GLPI_URL.split("/", 3)[:3])
            self.tryTelemetry()
            self.checkVersion()
            return True
        except Exception as e:
            print(e)
            print(chalk.red('[-] ' + Config.GLPI_URL + ' seems not accessible', bold=True))
            return False

    def getInfo(self):
        print(chalk.green('[+] Gathering basic information', bold=True))
        print(chalk.green('===============================\n', bold=True))
        if (self.checkServer()):
            return True
        return False
