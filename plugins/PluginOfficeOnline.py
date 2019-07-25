#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginOfficeOnline:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'officeonline')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)