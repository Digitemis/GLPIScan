#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginPrinterCounters:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'printercounters')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)