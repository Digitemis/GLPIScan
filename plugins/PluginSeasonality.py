#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginSeasonality:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'seasonality')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)