#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginBehaviors:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'behaviors')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)
