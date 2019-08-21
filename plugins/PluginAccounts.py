from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginAccounts:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'accounts')
        if version:
            Exploits().verifExploit(info[1], version)
