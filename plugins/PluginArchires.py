from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginArchires:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'archires')
        if version:
            Exploits().verifExploit(info[1], version)
