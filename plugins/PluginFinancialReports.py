from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginFinancialReports:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'financialreports')
        if version:
            Exploits().verifExploit(info[1], version)
