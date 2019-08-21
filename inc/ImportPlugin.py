from inc import Config

import importlib, inspect

class ImportPlugin:

    def importModule(self, plugin):
        if Config.DEBUG:
            print("[!] Import Plugin : " + plugin)
        module = importlib.import_module('plugins.' + plugin)
        for name, obj in inspect.getmembers(module):
            if name == plugin and inspect.isclass(obj):
                return obj()
        return None
