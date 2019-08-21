from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginAddressing:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'addressing')
        if version:
            Exploits().verifExploit(info[1], version)
