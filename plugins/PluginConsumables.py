from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginConsumables:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'consumables')
        if version:
            Exploits().verifExploit(info[1], version)
