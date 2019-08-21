from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginOrderManagement:

    def getVersion(self, info):
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.BASE_URL + info[0])
        r = requests.get(Config.BASE_URL + info[0], verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
        content = r.content.decode("utf-8")
        version = content[content.find('<num>') + len('<num>'):]
        version = version[:version.find('<')]
        print(chalk.white('\t[+] Version of [', bold=True) + chalk.yellow(info[1], bold=True) + chalk.white('] : [', bold=True) + chalk.yellow(version, bold=True) + chalk.white(']', bold=True))
        return version

    def initPlugin(self, info):
        version = self.getVersion(info)
        Exploits().verifExploit(info[1], version)
