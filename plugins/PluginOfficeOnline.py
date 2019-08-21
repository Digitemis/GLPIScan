from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginOfficeOnline:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'officeonline')
        if version:
            Exploits().verifExploit(info[1], version)