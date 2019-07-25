#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginDatabases:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'databases')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)
