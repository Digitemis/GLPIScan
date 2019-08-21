from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginDatabases:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'databases')
        if version:
            Exploits().verifExploit(info[1], version)
