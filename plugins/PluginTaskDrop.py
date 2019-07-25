#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginTaskDrop:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'taskdrop')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)