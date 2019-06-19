#!/usr/bin/python

import Config

import requests, chalk

class FilesCheck:

	def getFile(self, file):
		if Config.DEBUG:
			print("[DEBUG] GET : " + Config.BASE_URL + file)
		r = requests.get(Config.BASE_URL + file, verify=False)
		if (r.status_code == 200):
			print(chalk.white('[+] Interesting file found : ', bold=True) + chalk.red(Config.BASE_URL + file, bold=True))

	def getFolder(self, folder):
		if Config.DEBUG:
			print("[DEBUG] GET : " + Config.BASE_URL + folder)
		r = requests.get(Config.BASE_URL + folder, verify=False)
		if (r.status_code == 200):
			print(chalk.white('[+] Interesting folder found : ', bold=True) + chalk.red(Config.BASE_URL + folder, bold=True))

	def files(self):
		print(chalk.green('\n[+] Performing default files check', bold=True))
		print(chalk.green('==================================\n', bold=True))
		for file in Config.FILES:
			self.getFile(file)
		print(chalk.green('\n[+] Performing default folders check', bold=True))
		print(chalk.green('====================================\n', bold=True))
		for folder in Config.FOLDERS:
			self.getFolder(folder)