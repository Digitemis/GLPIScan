from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginTaskDrop:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'taskdrop')
        if version:
            Exploits().verifExploit(info[1], version)