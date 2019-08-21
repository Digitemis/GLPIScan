from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginWebApplications:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'webapplications')
        if version:
            Exploits().verifExploit(info[1], version)
