from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginDashboard:

    def getVersion(self, info):
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.BASE_URL + info[0])
        r = requests.get(Config.BASE_URL + info[0], verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
        content = r.content.decode("utf-8")
        if content.find('Version ') != -1:
            version = content[content.find('Version ') + len('Version '):]
            version = version[:version.find(':')]
            print(chalk.white('\t[+] Version of [', bold=True) + chalk.yellow(info[1], bold=True) + chalk.white('] : [', bold=True) + chalk.yellow(version, bold=True) + chalk.white(']', bold=True))
            return version
        return False

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'dashboard')
        if not version:
            version = self.getVersion(info)
        if version:
            Exploits().verifExploit(info[1], version)
        else:
            print(chalk.white('\t[-] Version not found : ', bold=True) + chalk.yellow(Config.BASE_URL + info[0], bold=True))
