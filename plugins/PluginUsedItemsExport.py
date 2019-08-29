from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginUsedItemsExport:

    def getVersion(self, info):
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.GLPI_URL + info[0])
        r = requests.get(Config.GLPI_URL + info[0], verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
        content = r.content.decode("utf-8")
        if content.find('<num>') != -1:
            version = content[content.find('<num>') + len('<num>'):]
            version = version[:version.find('<')]
            print(chalk.white('\t[+] Version of [', bold=True) + chalk.yellow(info[1], bold=True) + chalk.white('] : [', bold=True) + chalk.yellow(version, bold=True) + chalk.white(']', bold=True))
            return version
        return False

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'useditemsexport')
        if not version:
            version = self.getVersion(info)
        if version:
            Exploits().verifExploit(info[1], version)
        else:
            print(chalk.white('\t[-] Version not found : ', bold=True) + chalk.yellow(Config.GLPI_URL + info[0], bold=True))
