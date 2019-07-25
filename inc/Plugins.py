#!/usr/bin/python

import Config

from inc import ImportPlugin

import requests, chalk, json

class PluginsCheck:

	def getPlugin(self, plugin):
		if Config.DEBUG:
			print("[DEBUG] GET : " + Config.BASE_URL + plugin[0])
		r = requests.get(Config.BASE_URL + plugin[0], verify=False, proxies=Config.PROXY, headers=Config.HEADERS)
		if (r.status_code == 200):
			print(chalk.white('\n[+] Plugin [', bold=True) + chalk.yellow(plugin[1], bold=True) + chalk.white('] found !', bold=True))
			if plugin[3]:
				obj = ImportPlugin.ImportPlugin().importModule(plugin[3])
				obj.initPlugin(plugin)
			else:
				print(chalk.white('\t[-] Version not found : ', bold=True) + chalk.yellow(Config.BASE_URL + plugin[0], bold=True))


	def plugins(self):
		plugins = Config.PLUGINS
		print(chalk.green('\n[+] Performing Plugins check', bold=True))
		print(chalk.green('============================', bold=True))
		for plugin in plugins:
			self.getPlugin(plugin)
