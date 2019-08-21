from inc import Config

import chalk

class AjaxTelemetry:

    def getPluginVersion(self, info, name):
        try:
            for plugin in Config.AJAX_TELEMETRY['glpi']['plugins']:
                if plugin['key'] == name:
                    print(chalk.white('\t[+] Version of [', bold=True) + chalk.yellow(info[1], bold=True) + chalk.white('] : [', bold=True) + chalk.yellow(plugin['version'], bold=True) + chalk.white(']', bold=True))
                    return plugin['version']
        except:
            return False

    def getGLPIVersion(self):
        try:
            Config.VERSION = Config.AJAX_TELEMETRY['glpi']['version']
            return True
        except:
            return False
