from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginAppliances:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'appliances')
        if version:
            Exploits().verifExploit(info[1], version)
