#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginAppliances:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'appliances')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)
