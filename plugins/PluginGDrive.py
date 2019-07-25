#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginGDrive:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'gdrive')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)