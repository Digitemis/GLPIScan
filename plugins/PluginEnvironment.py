from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginEnvironment:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'environment')
        if version:
            Exploits().verifExploit(info[1], version)
