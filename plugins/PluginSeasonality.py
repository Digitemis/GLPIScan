from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginSeasonality:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'seasonality')
        if version:
            Exploits().verifExploit(info[1], version)