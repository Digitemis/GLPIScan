#!/usr/bin/python

import os, argparse, chalk
from inc import Config, Infos, Credentials, Files, Plugins

# Ugly way to clear shell
print("\033[H\033[J")
print(chalk.white(" ______     __         ______   __     ______     ______     ______     __   __   ", bold=True))
print(chalk.white("/\\  ___\\   /\\ \\       /\\  == \\ /\\ \\   /\\  ___\\   /\\  ___\\   /\\  __ \\   /\\ \"-.\\ \\  ", bold=True))
print(chalk.white("\\ \\ \\__ \\  \\ \\ \\____  \\ \\  __/ \\ \\ \\  \\ \\___  \\  \\ \\ \\____  \\ \\  __ \\  \\ \\ \\-.  \\ ", bold=True))
print(chalk.white(" \\ \\_____\\  \\ \\_____\\  \\ \\_\\    \\ \\_\\  \\/\\_____\\  \\ \\_____\\  \\ \\_\\ \\_\\  \\ \\_\\\"\\_\\", bold=True))
print(chalk.white("  \\/_____/   \\/_____/   \\/_/     \\/_/   \\/_____/   \\/_____/   \\/_/\\/_/   \\/_/ \\/_/", bold=True))
print(chalk.white("                                                      v1.1 contact[@]digitemis.com\n\n\n", bold=True))

def parsing():
	parser = argparse.ArgumentParser(description='GLPI Vulnerability Scanner.')
	parser.add_argument('-u', dest='url', metavar="url", required=True, help='URL of GLPI application')
	parser.add_argument('-a', dest='allcheck', action='store_true', default=False, help='Perform allcheck')
	parser.add_argument('-c', dest='credscheck', action='store_true', default=False, help='Perform Credential Check')
	parser.add_argument('-C', dest='credsfile', action='store_true', default=False, help='Perform Credential Check with specific wordlist (user:password)')
	parser.add_argument('-f', dest='filescheck', action='store_true', default=False, help='Perform Files Check')
	parser.add_argument('-p', dest='pluginscheck', action='store_true', default=False, help='Perform Plugin Check')
	parser.add_argument('-d', dest='debug', action='store_true', default=False, help='Debug mode')
	args = parser.parse_args()

	Config.DEBUG = args.debug
	Config.BASE_URL = args.url
	Config.ALLCHECK = args.allcheck
	Config.CREDSCHECK = args.credscheck
	Config.CREDSFILE = args.credsfile
	Config.FILESCHECK = args.filescheck
	Config.PLUGINSCHECK = args.pluginscheck

	if Config.DEBUG:
		print("[DEBUG] Debug mode : ON")
		print("[DEBUG] GLPI url : " + Config.BASE_URL)
		print("[DEBUG] Checking everything : " + str(Config.ALLCHECK))
		print("[DEBUG] Checking Default Creds : " + str(Config.CREDSCHECK))
		print("[DEBUG] Checking Default File : " + str(Config.FILESCHECK))
		print("[DEBUG] Checking Default Plugins : " + str(Config.PLUGINSCHECK))
		print("")

def main():
	parsing()
	print(chalk.white("[+] GLPI Scan start : " + Config.BASE_URL + "\n", bold=True))
	if (Infos.UrlCheck().getInfo()):
		if (Config.ALLCHECK or Config.CREDSCHECK):
			Credentials.CredentialsCheck().credentials()

		if (Config.ALLCHECK or Config.FILESCHECK):
			Files.FilesCheck().files()

		if (Config.ALLCHECK or Config.PLUGINSCHECK):
			Plugins.PluginsCheck().plugins()

main()
