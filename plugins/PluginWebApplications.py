#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginWebApplications:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'webapplications')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)
