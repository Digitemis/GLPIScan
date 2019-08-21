from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginOCSInventoryng:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'ocsinventoryng')
        if version:
            Exploits().verifExploit(info[1], version)
