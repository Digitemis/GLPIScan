#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginOCSInventoryng:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'ocsinventoryng')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)
