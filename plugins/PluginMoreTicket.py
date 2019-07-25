#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginMoreTicket:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'moreticket')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)
