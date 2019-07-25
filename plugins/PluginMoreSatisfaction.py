#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginMoreSatisfaction:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'satisfaction')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)