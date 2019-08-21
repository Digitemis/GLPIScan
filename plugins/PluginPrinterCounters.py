from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginPrinterCounters:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'printercounters')
        if version:
            Exploits().verifExploit(info[1], version)