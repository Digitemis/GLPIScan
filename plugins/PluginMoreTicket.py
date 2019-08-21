from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginMoreTicket:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'moreticket')
        if version:
            Exploits().verifExploit(info[1], version)
