import requests
requests.packages.urllib3.disable_warnings() 

# Debug mode is disable by default
DEBUG = False

# Base URL of the scanned GLPI
BASE_URL = ""

# Root folder of the scanned GLPI
ROOT_DOC = "/"

# Version of the scanned GLPI
VERSION = ""

# By default do not perfom all checks on GLPI
ALLCHECK = False

# By default do not perfom credentials checks on GLPI
CREDSCHECK = False

# By default do not perfom files checks on GLPI
FILESCHECK = False

# By default do not perfom plugins checks on GLPI
PLUGINSCHECK = False

COOKIE = ""

FILES = ['/ajax/telemetry.php',
		'/CHANGELOG.md',
		'/status.php',
		'/files/_log/cron.log',
		'/files/_log/event.log',
		'/files/_log/php-errors.log']

FOLDERS = ['/files/',
		   '/files/_dumps/',
		   '/plugins/']

# ['USER', 'PASSWORD']
USERS = [['glpi','glpi'],
		 ['post-only','postonly'],
		 ['tech','tech'],
		 ['normal', 'normal']]

# ['URL_VERIFY', 'PLUGIN_NAME', 'PLUGIN_URL', 'PLUGIN_CLASS']
PLUGINS = [['/plugins/addressing/LICENSE', 'IP Report', 'https://plugins.glpi-project.org/#/plugin/addressing', False],
		   ['/plugins/fusioninventory/js/footer.js', 'FusionInventory', 'https://plugins.glpi-project.org/#/plugin/fusioninventory', 'PluginFusionInventory'],
		   ['/plugins/dashboard/changelog.txt', 'Dashboard', 'https://plugins.glpi-project.org/#/plugin/dashboard', 'PluginDashboard'],
		   ['/plugins/datainjection/datainjection.xml', 'Data Injection', 'https://plugins.glpi-project.org/#/plugin/datainjection', 'PluginDataInjection'],
		   ['/plugins/fields/plugin.xml', 'Fields', 'https://plugins.glpi-project.org/#/plugin/field', 'PluginFields'],
		   ['/plugins/formcreator/package.json', 'FormCreator', 'https://plugins.glpi-project.org/#/plugin/formcreator', 'PluginFormCreator'],
		   ['/plugins/genericobject/genericobject.xml', 'Generic Objects Management', 'https://plugins.glpi-project.org/#/plugin/genericobject', 'PluginGenericObjectsManagement'],
		   ['/plugins/mreporting/mreporting.xml', 'More Reporting', 'https://plugins.glpi-project.org/#/plugin/mreporting', 'PluginMoreReporting'],
		   ['/plugins/ocsinventoryng/docs/CHANGELOG.txt', 'OCS Inventory NG', 'https://plugins.glpi-project.org/#/plugin/ocsinventoryng', False],
		   ['/plugins/reports/LICENSE', 'Reports', 'https://plugins.glpi-project.org/#/plugin/reports', False],
		   ['/plugins/pdf/LICENSE', 'PDF', 'https://plugins.glpi-project.org/#/plugin/pdf', False],
		   ['/plugins/archires/LICENSE', 'Network Architecture', 'https://plugins.glpi-project.org/#/plugin/archires', False],
		   ['/plugins/room/room.xml', 'Room Management', 'https://plugins.glpi-project.org/#/plugin/room', 'PluginRoom'],
		   ['/plugins/racks/locales/glpi.pot', 'Racks / Bays Management', 'https://plugins.glpi-project.org/#/plugin/racks', 'PluginRacks'],
		   ['/plugins/manageentities/LICENSE', 'Entities Management', 'https://plugins.glpi-project.org/#/plugin/manageentities', False],
		   ['/plugins/accounts/LICENSE', 'Accounts Inventory', 'https://plugins.glpi-project.org/#/plugin/accounts', False],
		   ['/plugins/appliances/LICENSE', 'Appliances Inventory', 'https://plugins.glpi-project.org/#/plugin/appliances', False],
		   ['/plugins/badges/locales/glpi.pot', 'Badges Inventory', 'https://plugins.glpi-project.org/#/plugin/badges', 'PluginBadgesInventory'],
		   ['/plugins/certificates/LICENSE', 'Certificates Inventory', 'https://plugins.glpi-project.org/#/plugin/certificates', False],
		   ['/plugins/databases/LICENSE', 'Databases Inventory', 'https://plugins.glpi-project.org/#/plugin/databases', False],
		   ['/plugins/domains/locales/glpi.pot', 'Domains Inventory', 'https://plugins.glpi-project.org/#/plugin/domains', 'PluginDomainsInventory'],
		   ['/plugins/financialreports/LICENSE', 'Financial Reports', 'https://plugins.glpi-project.org/#/plugin/financialreports', False],
		   ['/plugins/environment/LICENSE', 'Meta-Plugin Environment', 'https://plugins.glpi-project.org/#/plugin/environment', False],
		   ['/plugins/shellcommands/locales/glpi.pot', 'Launch Shell Commands', 'https://plugins.glpi-project.org/#/plugin/shellcommands', 'PluginLaunchShellCommands'],
		   ['/plugins/webapplications/LICENSE', 'Web Applications Inventory', 'https://plugins.glpi-project.org/#/plugin/webapplications', False],
		   ['/plugins/order/plugin.xml', 'Order Management', 'https://plugins.glpi-project.org/#/plugin/order', 'PluginOrderManagement'],
		   ['/plugins/uninstall/uninstall.xml', 'Uninstall', 'https://plugins.glpi-project.org/#/plugin/uninstall', 'PluginUninstall'],
		   ['/plugins/geninventorynumber/plugin.xml', 'Inventory Number Generation', 'https://plugins.glpi-project.org/#/plugin/geninventorynumber', 'PluginInventoryNumberGeneration'],
		   ['/plugins/behaviors/LICENSE', 'Behaviors', 'https://plugins.glpi-project.org/#/plugin/behaviors', False],
		   ['/plugins/barcode/barcode.xml', 'Barcode', 'https://plugins.glpi-project.org/#/plugin/barcode', 'PluginBarcode'],
		   ['/plugins/positions/locales/glpi.pot', 'Cartography', 'https://plugins.glpi-project.org/#/plugin/positions', 'PluginCartography'],
		   ['/plugins/typology/locales/glpi.pot', 'Typology', 'https://plugins.glpi-project.org/#/plugin/typology', 'PluginTypology'],
		   ['/plugins/mask/mask.xml', 'Mask', 'https://plugins.glpi-project.org/#/plugin/mask', 'PluginMask'],
		   ['/plugins/surveyticket/LICENSE', 'SurveyTicket', 'https://plugins.glpi-project.org/#/plugin/surveyticket', False],
		   ['/plugins/mantis/mantis.xml', 'MantisBT synchronization', 'https://plugins.glpi-project.org/#/plugin/mantis', 'PluginMantis'],
		   ['/plugins/reservation/LICENCE', 'Reservation', 'https://plugins.glpi-project.org/#/plugin/reservation', False],
		   ['/plugins/timezones/timezones.xml', 'Timezones', 'https://plugins.glpi-project.org/#/plugin/timezones', 'PluginTimezones'],
		   ['/plugins/sccm/sccm.xml', 'SCCM', 'https://plugins.glpi-project.org/#/plugin/sccm', 'PluginSCCM'],
		   ['/plugins/tag/plugin.xml', 'Tag', 'https://plugins.glpi-project.org/#/plugin/tag', 'PluginTag'],
		   ['/plugins/news/plugin.xml', 'News', 'https://plugins.glpi-project.org/#/plugin/news', 'PluginNews'],
		   ['/plugins/purgelogs/plugin.xml', 'Historical purge', 'https://plugins.glpi-project.org/#/plugin/purgelogs', 'PluginHistoricalPurge'],
		   ['/plugins/escalade/escalade.xml', 'Escalade', 'https://plugins.glpi-project.org/#/plugin/escalade', 'PluginEscalade'],
		   ['/plugins/moreticket/LICENSE', 'Moreticket', 'https://plugins.glpi-project.org/#/plugin/moreticket', False],
		   ['/plugins/itilcategorygroups/itilcategorygroups.xm	l', 'ItilCategory Groups', 'https://plugins.glpi-project.org/#/plugin/itilcategorygroups', 'PluginItilCategoryGroups'],
		   ['/plugins/consumables/LICENSE', 'Consumables', 'https://plugins.glpi-project.org/#/plugin/consumables', False],
		   ['/plugins/printercounters/LICENSE', 'PrinterCounters', 'https://plugins.glpi-project.org/#/plugin/printercounters', False],
		   ['/plugins/processmaker/processmaker.xml', 'Processmaker', 'https://plugins.glpi-project.org/#/plugin/processmaker', 'PluginProcessmaker'],
		   ['/plugins/seasonality/README.md', 'Seasonality', 'https://plugins.glpi-project.org/#/plugin/seasonality', False],
		   ['/plugins/tasklists/locales/glpi.pot', 'Tasks List (Kanban)', 'https://plugins.glpi-project.org/#/plugin/tasklists', 'PluginTasksList'],
		   ['/plugins/mailanalyzer/mailanalyzer.xml', 'Mail Analyzer', 'https://plugins.glpi-project.org/#/plugin/mailanalyzer', 'PluginMailAnalyzer'],
		   ['/plugins/mydashboard/locales/glpi.pot', 'My Dashboard', 'https://plugins.glpi-project.org/#/plugin/mydashboard', 'PluginMyDashboard'],
		   ['/plugins/timelineticket/locales/glpi.pot', 'Timelineticket', 'https://plugins.glpi-project.org/#/plugin/timelineticket', 'PluginTimelineticket'],
		   ['/plugins/airwatch/airwatch.xml', 'Airwatch connector', 'https://plugins.glpi-project.org/#/plugin/airwatch', 'PluginAirwatchConnector'],
		   ['/plugins/archifun/funcarea.xml', 'Functional Areas', 'https://plugins.glpi-project.org/#/plugin/archifun', 'PluginFunctionalAreas'],
		   ['/plugins/useditemsexport/plugin.xml', 'Used items export', 'https://plugins.glpi-project.org/#/plugin/useditemsexport', 'PluginUsedItemsExport'],
		   ['/plugins/nebackup/nebackup.xml', 'Network Equipment Backup', 'https://plugins.glpi-project.org/#/plugin/nebackup', 'PluginNetworkEquipmentBackup'],
		   ['/plugins/openvas/openvas.xml', 'OpenVAS', 'https://plugins.glpi-project.org/#/plugin/openvas', 'PluginOpenVAS'],
		   ['/plugins/browsernotification/browsernotification.xml', 'Browser Notification', 'https://plugins.glpi-project.org/#/plugin/browsernotification', 'PluginBrowserNotification'],
		   ['/plugins/credit/plugin.xml', 'Credit', 'https://plugins.glpi-project.org/#/plugin/credit', 'PluginCredit'],
		   ['/plugins/xivo/xivo.xml', 'xivo', 'https://plugins.glpi-project.org/#/plugin/xivo', 'PluginXivo'],
		   ['/plugins/glpi2mdt/glpi2mdt.xml', 'GLPI to MDT connector', 'https://plugins.glpi-project.org/#/plugin/glpi2mdt', 'PluginMDTConnector'],
		   ['/plugins/telegrambot/telegrambot.xml', 'TelegramBot', 'https://plugins.glpi-project.org/#/plugin/telegrambot', 'PluginTelegramBot'],
		   ['/plugins/cleanarchivedemails/cleanarchivedemails.xml', 'Clean Archived Emails', 'https://plugins.glpi-project.org/#/plugin/cleanarchivedemails', 'PluginCleanArchivedEmails'],
		   ['/plugins/officeonline/js/officeonline.js', 'Office Online', 'https://plugins.glpi-project.org/#/plugin/officeonline', False],
		   ['/plugins/satisfaction/satisfaction.js', 'More satisfaction', 'https://plugins.glpi-project.org/#/plugin/satisfaction', False],
		   ['/plugins/gdrive/README.md', 'GDrive', 'https://plugins.glpi-project.org/#/plugin/GDrive', False],
		   ['/plugins/archisw/archisw.xml', 'Apps structure inventory', 'https://plugins.glpi-project.org/#/plugin/archisw', 'PluginAppsStructureInventory'],
		   ['/plugins/dataflows/dataflows.xml', 'Dataflows inventory', 'https://plugins.glpi-project.org/#/plugin/dataflows', 'PluginDataflowsInventory'],
		   ['/plugins/statecheck/statecheck.xml', 'Statecheck', 'https://plugins.glpi-project.org/#/plugin/statecheck', 'PluginStatecheck'],
		   ['/plugins/archimap/archimap.xml', 'Diagrams', 'https://plugins.glpi-project.org/#/plugin/archimap', 'PluginDiagrams'],
		   ['/plugins/metabase/metabase.xml', 'Metabase', 'https://plugins.glpi-project.org/#/plugin/metabase', 'PluginMetabase'],
		   ['/plugins/orderservice/orderservice.xml', 'Order Service', 'https://plugins.glpi-project.org/#/plugin/orderservice', 'PluginOrderService'],
		   ['/plugins/glpicheckingversion/glpicheckingversion.xml', 'GLPI Checking Version', 'https://plugins.glpi-project.org/#/plugin/glpicheckingversion', 'PluginGLPICheckingVersion'],
		   ['/plugins/taskdrop/LICENSE', 'Task n Drop', 'https://plugins.glpi-project.org/#/plugin/TaskDrop', False],
		   ['/plugins/impacts/impacts.xml', 'Impacts', 'https://plugins.glpi-project.org/#/plugin/impacts', 'PluginImpacts'],
		   ]

# ['VENDOR', ['OPERANDE', 'VERSION'], 'DESC' ,'LINK', 'CVE']
CVE = [
	   ['GLPI', [['<', '0.80.2']], 'Sensitive information disclosure' ,'https://nvd.nist.gov/vuln/detail/CVE-2011-2720', 'CVE-2011-2720'],
	   ['GLPI', [['>=', '0.78'], ['<=', '0.80.61']], 'Remote file inclusion vulnerability in front/popup.php' ,'https://seclists.org/fulldisclosure/2012/Feb/157', 'CVE-2012-1037'],
	   ['GLPI', [['<', '0.83.3']], 'Cross-site request forgery (CSRF)' ,'http://www.prajalkulkarni.com/2012/10/multiple-csrf-and-xss-vulnerabilities.html', 'CVE-2012-4002'],
	   ['GLPI', [['<', '0.83.3']],'Multiple cross-site scripting', 'http://www.prajalkulkarni.com/2012/10/multiple-csrf-and-xss-vulnerabilities.html', 'CVE-2012-4003'],
	   ['GLPI', [['=', '0.83.9']], 'Unserialize() Remote Code Execution' ,'https://www.exploit-db.com/exploits/26530', 'CVE-2013-2225'],
	   ['GLPI', [['>=', '0.83'], ['<=', '0.83.8']], 'Multiple Error-based SQL Injection' ,'https://downloads.securityfocus.com/vulnerabilities/exploits/60693.txt', 'CVE-2013-2226'],
	   ['GLPI', [['<', '0.84.2']], 'GLPI install.php Remote Command Execution' ,'https://www.exploit-db.com/exploits/28483', 'CVE-2013-5696'],
	   ['GLPI', [['<', '0.84.7']], 'Access control defecting on cost criteria' ,'https://nvd.nist.gov/vuln/detail/CVE-2014-5032', 'CVE-2014-5032'],
	   ['GLPI', [['<', '0.84.8']], 'Directory traversal vulnerability in inc/autoload.function.php' ,'http://tlk.tuxfamily.org/doku.php?id=writeup:cve-2014-8360', 'CVE-2014-8360'],
	   ['GLPI', [['<', '0.85.1']], 'Blind SQL Injection in ajax/getDropdownValue.php' ,'https://www.exploit-db.com/exploits/35528', 'CVE-2014-9258'],
	   ['GLPI', [['<=', '0.85.2']], 'Privilege escalation' ,'https://seclists.org/fulldisclosure/2015/Feb/71', 'CVE-2015-7685'],
	   ['GLPI', [['>=', '0.85.0'], ['<=', '0.85.2']], 'Remote Code Execution' ,'https://seclists.org/fulldisclosure/2015/Feb/71', 'CVE-2015-7684'],
	   ['GLPI', [['=', '0.90.4']], 'Cross-Site Request Forgery' ,'https://nvd.nist.gov/vuln/detail/CVE-2016-7507', 'CVE-2016-7507'],
	   ['GLPI', [['=', '0.90.4']], 'Multiple SQL injection' ,'https://www.exploit-db.com/exploits/42262', 'CVE-2016-7508'],
	   ['GLPI', [['=', '0.90.4']], 'Store XSS in Ticket' ,'https://nvd.nist.gov/vuln/detail/CVE-2016-7509', 'CVE-2016-7509'],
	   ['GLPI', [['<=', '9.1.5']], 'front/backup.php file denial of service' ,'https://nvd.nist.gov/vuln/detail/CVE-2017-11183', 'CVE-2017-11183'],
	   ['GLPI', [['<', '9.1.5']], 'SQL injection in front/devicesoundcard.php' ,'https://github.com/glpi-project/glpi/issues/2450', 'CVE-2017-11183'],
	   ['GLPI', [['<=', '9.2.1']], 'Cross Site Scripting in /front/preference.php' ,'https://members.backbox.org/glpi-9-2-1-multiple-vulnerabilities/', 'CVE-2018-7563'],
	   ['GLPI', [['<', '9.1.5']], 'SQL injection in front/devicesoundcard.php' ,'https://github.com/glpi-project/glpi/issues/2449', 'CVE-2017-11184'],
	   ['GLPI', [['<', '9.1.5']], 'SQL injection in ajax/getDropdownValue.php' ,'https://github.com/glpi-project/glpi/issues/2456', 'CVE-2017-11329'],
	   ['GLPI', [['<', '9.1.5.1']], 'SQL injection in ajax/common.tabs.php' ,'https://github.com/glpi-project/glpi/issues/2475', 'CVE-2017-11474'],
	   ['GLPI', [['<', '9.1.5.1']], 'SQL injection in front/rulesengine.test.php' ,'https://github.com/glpi-project/glpi/issues/2476', 'CVE-2017-11475'],
	   ['GLPI', [['<=', '9.2.1']], 'Remote code execution' ,'https://github.com/bowline90/RemoteCodeUploadGLPI', 'CVE-2018-7562'],
	   ['GLPI', [['<=', '9.3.3']], 'Pre-authenticated SQL injection' ,'https://www.synacktiv.com/ressources/advisories/GLPI_9.3.3_SQL_Injection.pdf', 'CVE-2019-10232'],
	   ['GLPI', [['<=', '9.4.1.1']], 'Type juggling authentication bypass', 'https://www.synacktiv.com/ressources/GLPI_9.4.0_Type_juggling_auth_bypass.pdf', 'CVE-2019-10231'],
	   ['GLPI', [['<=', '9.4.1.1']], 'Timing attack user enumeration', 'https://www.synacktiv.com/ressources/GLPI_9.4.0_Timing_attack_user_enumeration.pdf', 'CVE-2019-10233'],
	   ['FusionInventory', [['<=', '9.4.0']], 'Arbitrary PHP function call', 'https://www.synacktiv.com/ressources/GLPI_FusionInventory_9.4.0_Arbitrary_call_user_func_array.pdf', 'CVE-2019-10477']]
