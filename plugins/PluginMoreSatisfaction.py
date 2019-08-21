from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginMoreSatisfaction:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'satisfaction')
        if version:
            Exploits().verifExploit(info[1], version)