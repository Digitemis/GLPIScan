from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginPdf:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'pdf')
        if version:
            Exploits().verifExploit(info[1], version)
