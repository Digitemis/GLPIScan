from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginReservation:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'reservation')
        if version:
            Exploits().verifExploit(info[1], version)
