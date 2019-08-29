from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginMoreSatisfaction:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'satisfaction')
        if version:
            Exploits().verifExploit(info[1], version)
        else:
            print(chalk.white('\t[-] Version not found : ', bold=True) + chalk.yellow(Config.GLPI_URL + info[0], bold=True))
