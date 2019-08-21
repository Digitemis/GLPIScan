from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginGDrive:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'gdrive')
        if version:
            Exploits().verifExploit(info[1], version)