from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginFinancialReports:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'financialreports')
        if version:
            Exploits().verifExploit(info[1], version)
        else:
            print(chalk.white('\t[-] Version not found : ', bold=True) + chalk.yellow(Config.GLPI_URL + info[0], bold=True))
