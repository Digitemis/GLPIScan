#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginConsumables:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'consumables')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)
