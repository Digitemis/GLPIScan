from inc import Config, ImportPlugin

import requests, chalk, json

class PluginsCheck:

    def getPlugin(self, plugin):
        if Config.DEBUG:
            print("[DEBUG] GET : " + Config.GLPI_URL + plugin[0])
        pluginfolder = "/".join(plugin[0].split("/", 3)[:3]) 
        r = requests.get(Config.GLPI_URL + pluginfolder, verify=False, proxies=Config.PROXY, headers=Config.HEADERS, allow_redirects=False)
        if (r.status_code == 301):
            print(chalk.white('\n[+] Plugin [', bold=True) + chalk.yellow(plugin[1], bold=True) + chalk.white('] found !', bold=True))
            obj = ImportPlugin().importModule(plugin[3])
            obj.initPlugin(plugin)

    def plugins(self):
        plugins = Config.PLUGINS
        print(chalk.green('\n[+] Performing Plugins check', bold=True))
        print(chalk.green('============================', bold=True))
        for plugin in plugins:
            self.getPlugin(plugin)
