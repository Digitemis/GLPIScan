from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginArchires:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'archires')
        if version:
            Exploits().verifExploit(info[1], version)
        else:
            print(chalk.white('\t[-] Version not found : ', bold=True) + chalk.yellow(Config.GLPI_URL + info[0], bold=True))
