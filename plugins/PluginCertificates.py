from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginCertificates:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'certificates')
        if version:
            Exploits().verifExploit(info[1], version)
