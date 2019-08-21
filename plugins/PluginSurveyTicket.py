from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginSurveyTicket:

    def initPlugin(self, info):
        version = AjaxTelemetry().getPluginVersion(info, 'surveyticket')
        if version:
            Exploits().verifExploit(info[1], version)
