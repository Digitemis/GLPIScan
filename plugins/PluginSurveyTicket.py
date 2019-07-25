#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginSurveyTicket:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'surveyticket')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)
