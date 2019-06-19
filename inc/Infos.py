#!/usr/bin/python

import Config, Exploits

from urlparse import urlparse
import requests, json, chalk

class UrlCheck:

	def getURLBase(self, content):
		if (content.find("'url_base': '") != -1):
			url_base = content[content.find("'url_base': '")+len("'url_base': '"):]
			url_base = url_base[:url_base.find("'")]
			Config.BASE_URL = url_base
		print(chalk.white('[+] url_base : ', bold=True) + chalk.yellow(Config.BASE_URL, bold=True))

	def getRootDoc(self, content):
		if (content.find("'root_doc': '") != -1):
			root_doc = content[content.find("'root_doc': '")+len("'root_doc': '"):]
			root_doc = root_doc[:root_doc.find("'")]
			Config.ROOT_DOC = root_doc
		print(chalk.white('[+] root_doc : ', bold=True) + chalk.yellow(Config.ROOT_DOC, bold=True))

	def getVersion(self):
		if Config.DEBUG:
			print("[DEBUG] GET : " + Config.BASE_URL)
		r = requests.get(Config.BASE_URL, verify=False)
		version = r.content[r.content.find('?v=')+len('?v='):]
		version = version[:version.find('"')]
		Config.VERSION = version
		print(chalk.white('[+] Version of GLPI : ', bold=True) + chalk.yellow(Config.VERSION, bold=True))
		Exploits.ExploitsCheck().verifExploit('GLPI', Config.VERSION)

	def checkServer(self):
		try:
			if Config.DEBUG:
				print("[DEBUG] GET : " + Config.BASE_URL)
			r = requests.get(Config.BASE_URL, timeout=10, verify=False)
			print(chalk.white('[+] Server Header : ', bold=True) + chalk.yellow(r.headers['Server'], bold=True))
			self.getURLBase(r.content)
			self.getRootDoc(r.content)
			self.getVersion()
			return True
		except Exception as e:
			print(chalk.red('[-] ' + Config.BASE_URL + ' seems not accessible', bold=True))
			return False

	def getInfo(self):
		print(chalk.green('[+] Gathering basic information', bold=True))
		print(chalk.green('===============================\n', bold=True))
		if (self.checkServer()):
			return True
		return False