#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginManufacturersImports:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'manufacturersimports')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)
