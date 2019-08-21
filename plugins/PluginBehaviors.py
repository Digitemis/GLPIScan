from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginBehaviors:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'behaviors')
        if version:
            Exploits().verifExploit(info[1], version)
