#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginReservation:

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'reservation')
		if version:
			Exploits.ExploitsCheck().verifExploit(info[1], version)
