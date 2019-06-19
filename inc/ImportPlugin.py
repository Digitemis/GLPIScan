#!/usr/bin/python

import Config

import importlib, inspect

class ImportPlugin:

	def importModule(self, name):
		if Config.DEBUG:
			print("[!] Import Plugin : " + name)
		module = importlib.import_module('plugins.' + name)
		for name, obj in inspect.getmembers(module):
			if inspect.isclass(obj):
				return obj()
		return None