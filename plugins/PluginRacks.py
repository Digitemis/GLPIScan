#!/usr/bin/python

from inc import Config, Exploits, AjaxTelemetry

import requests, chalk

class PluginRacks:

	def getVersion(self, info):
		if Config.DEBUG:
			print("[DEBUG] GET : " + Config.BASE_URL + info[0])
		r = requests.get(Config.BASE_URL + info[0], verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
		content = r.content
		version = content[content.find('Racks plugin ') + len('Racks plugin '):]
		version = version[:version.find('\\')]
		print(chalk.white('\t[+] Version of [', bold=True) + chalk.yellow(info[1], bold=True) + chalk.white('] : [', bold=True) + chalk.yellow(version, bold=True) + chalk.white(']', bold=True))
 		return version

	def initPlugin(self, info):
		version = AjaxTelemetry.AjaxTelemetry().getPluginVersion(info, 'racks')
		if not version:
			version = self.getVersion(info)
		Exploits.ExploitsCheck().verifExploit(info[1], version)
