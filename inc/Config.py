import requests
requests.packages.urllib3.disable_warnings() 

# Debug mode is disable by default
DEBUG = False

# Base URL of the scanned GLPI
GLPI_URL = ""

# Root folder of the scanned GLPI
SERVER_ROOT = ""

# Version of the scanned GLPI
VERSION = ""

# Default value of JSON Telemetry page
AJAX_TELEMETRY = {}

# By default do not perfom all checks on GLPI
ALLCHECK = False

# By default do not perfom credentials checks on GLPI
CREDSCHECK = False

# By default do not perfom credentials checks on GLPI
CREDSFILE = False

# By default do not perfom files checks on GLPI
FILESCHECK = False

# By default do not perfom plugins checks on GLPI
PLUGINSCHECK = False

# Proxy configuration
PROXY = {"http"  : "", "https" : ""}

# Custom header configuration {"header" : "value"}
HEADERS = {}

COOKIE = ""

SERVER = ['/phpmyadmin',
        '/adminer',
        '/ocsreport',
        ]

FILES = ['/ajax/telemetry.php',
        '/CHANGELOG.md',
        '/status.php',
        '/files/_log/cron.log',
        '/files/_log/event.log',
        '/files/_log/php-errors.log',
        '/files/_log/mail.log',
        '/files/_log/sql-errors.log',
        '/vendor/htmlawed/htmlawed/htmLawedTest.php'

        ]

FOLDERS = ['/files',
           '/files/_dumps',
           '/files/_uploads',
           '/plugins',
           '/plugins_old',
           ]

# ['USER', 'PASSWORD']
USERS = [['glpi','glpi'],
         ['post-only','postonly'],
         ['tech','tech'],
         ['normal', 'normal'],
         ['admin', 'admin']
         ]

# ['URL_VERIFY', 'PLUGIN_NAME', 'PLUGIN_URL', 'PLUGIN_CLASS']
PLUGINS = [['/plugins/addressing/LICENSE', 'IP Report', 'https://plugins.glpi-project.org/#/plugin/addressing', 'PluginAddressing'],
           ['/plugins/fusioninventory/js/footer.js', 'FusionInventory', 'https://plugins.glpi-project.org/#/plugin/fusioninventory', 'PluginFusionInventory'],
           ['/plugins/dashboard/changelog.txt', 'Dashboard', 'https://plugins.glpi-project.org/#/plugin/dashboard', 'PluginDashboard'],
           ['/plugins/datainjection/datainjection.xml', 'Data Injection', 'https://plugins.glpi-project.org/#/plugin/datainjection', 'PluginDataInjection'],
           ['/plugins/fields/plugin.xml', 'Fields', 'https://plugins.glpi-project.org/#/plugin/field', 'PluginFields'],
           ['/plugins/formcreator/package.json', 'FormCreator', 'https://plugins.glpi-project.org/#/plugin/formcreator', 'PluginFormCreator'],
           ['/plugins/genericobject/genericobject.xml', 'Generic Objects Management', 'https://plugins.glpi-project.org/#/plugin/genericobject', 'PluginGenericObjectsManagement'],
           ['/plugins/mreporting/mreporting.xml', 'More Reporting', 'https://plugins.glpi-project.org/#/plugin/mreporting', 'PluginMoreReporting'],
           ['/plugins/ocsinventoryng/docs/CHANGELOG.txt', 'OCS Inventory NG', 'https://plugins.glpi-project.org/#/plugin/ocsinventoryng', 'PluginOCSInventoryng'],
           ['/plugins/reports/LICENSE', 'Reports', 'https://plugins.glpi-project.org/#/plugin/reports', 'PluginReports'],
           ['/plugins/pdf/LICENSE', 'PDF', 'https://plugins.glpi-project.org/#/plugin/pdf', 'PluginPdf'],
           ['/plugins/archires/LICENSE', 'Network Architecture', 'https://plugins.glpi-project.org/#/plugin/archires', 'PluginArchires'],
           ['/plugins/room/room.xml', 'Room Management', 'https://plugins.glpi-project.org/#/plugin/room', 'PluginRoom'],
           ['/plugins/racks/locales/glpi.pot', 'Racks / Bays Management', 'https://plugins.glpi-project.org/#/plugin/racks', 'PluginRacks'],
           ['/plugins/manageentities/LICENSE', 'Entities Management', 'https://plugins.glpi-project.org/#/plugin/manageentities', 'PluginManageEntities'],
           ['/plugins/accounts/LICENSE', 'Accounts Inventory', 'https://plugins.glpi-project.org/#/plugin/accounts', 'PluginAccounts'],
           ['/plugins/appliances/LICENSE', 'Appliances Inventory', 'https://plugins.glpi-project.org/#/plugin/appliances', 'PluginAppliances'],
           ['/plugins/badges/locales/glpi.pot', 'Badges Inventory', 'https://plugins.glpi-project.org/#/plugin/badges', 'PluginBadgesInventory'],
           ['/plugins/certificates/LICENSE', 'Certificates Inventory', 'https://plugins.glpi-project.org/#/plugin/certificates', 'PluginCertificates'],
           ['/plugins/databases/LICENSE', 'Databases Inventory', 'https://plugins.glpi-project.org/#/plugin/databases', 'PluginDatabases'],
           ['/plugins/domains/locales/glpi.pot', 'Domains Inventory', 'https://plugins.glpi-project.org/#/plugin/domains', 'PluginDomainsInventory'],
           ['/plugins/financialreports/LICENSE', 'Financial Reports', 'https://plugins.glpi-project.org/#/plugin/financialreports', 'PluginFinancialReports'],
           ['/plugins/environment/LICENSE', 'Meta-Plugin Environment', 'https://plugins.glpi-project.org/#/plugin/environment',  'PluginEnvironment'],
           ['/plugins/shellcommands/locales/glpi.pot', 'Launch Shell Commands', 'https://plugins.glpi-project.org/#/plugin/shellcommands', 'PluginLaunchShellCommands'],
           ['/plugins/webapplications/LICENSE', 'Web Applications Inventory', 'https://plugins.glpi-project.org/#/plugin/webapplications', 'PluginWebApplications'],
           ['/plugins/order/plugin.xml', 'Order Management', 'https://plugins.glpi-project.org/#/plugin/order', 'PluginOrderManagement'],
           ['/plugins/uninstall/uninstall.xml', 'Uninstall', 'https://plugins.glpi-project.org/#/plugin/uninstall', 'PluginUninstall'],
           ['/plugins/geninventorynumber/plugin.xml', 'Inventory Number Generation', 'https://plugins.glpi-project.org/#/plugin/geninventorynumber', 'PluginInventoryNumberGeneration'],
           ['/plugins/behaviors/LICENSE', 'Behaviors', 'https://plugins.glpi-project.org/#/plugin/behaviors', 'PluginBehaviors'],
           ['/plugins/barcode/barcode.xml', 'Barcode', 'https://plugins.glpi-project.org/#/plugin/barcode', 'PluginBarcode'],
           ['/plugins/positions/locales/glpi.pot', 'Cartography', 'https://plugins.glpi-project.org/#/plugin/positions', 'PluginCartography'],
           ['/plugins/typology/locales/glpi.pot', 'Typology', 'https://plugins.glpi-project.org/#/plugin/typology', 'PluginTypology'],
           ['/plugins/mask/mask.xml', 'Mask', 'https://plugins.glpi-project.org/#/plugin/mask', 'PluginMask'],
           ['/plugins/surveyticket/LICENSE', 'SurveyTicket', 'https://plugins.glpi-project.org/#/plugin/surveyticket', 'PluginSurveyTicket'],
           ['/plugins/mantis/mantis.xml', 'MantisBT synchronization', 'https://plugins.glpi-project.org/#/plugin/mantis', 'PluginMantis'],
           ['/plugins/reservation/LICENCE', 'Reservation', 'https://plugins.glpi-project.org/#/plugin/reservation', 'PluginReservation'],
           ['/plugins/timezones/timezones.xml', 'Timezones', 'https://plugins.glpi-project.org/#/plugin/timezones', 'PluginTimezones'],
           ['/plugins/sccm/sccm.xml', 'SCCM', 'https://plugins.glpi-project.org/#/plugin/sccm', 'PluginSCCM'],
           ['/plugins/tag/plugin.xml', 'Tag', 'https://plugins.glpi-project.org/#/plugin/tag', 'PluginTag'],
           ['/plugins/news/plugin.xml', 'News', 'https://plugins.glpi-project.org/#/plugin/news', 'PluginNews'],
           ['/plugins/purgelogs/plugin.xml', 'Historical purge', 'https://plugins.glpi-project.org/#/plugin/purgelogs', 'PluginHistoricalPurge'],
           ['/plugins/escalade/escalade.xml', 'Escalade', 'https://plugins.glpi-project.org/#/plugin/escalade', 'PluginEscalade'],
           ['/plugins/moreticket/LICENSE', 'Moreticket', 'https://plugins.glpi-project.org/#/plugin/moreticket', 'PluginMoreTicket'],
           ['/plugins/itilcategorygroups/itilcategorygroups.xml', 'ItilCategory Groups', 'https://plugins.glpi-project.org/#/plugin/itilcategorygroups', 'PluginItilCategoryGroups'],
           ['/plugins/consumables/LICENSE', 'Consumables', 'https://plugins.glpi-project.org/#/plugin/consumables', 'PluginConsumables'],
           ['/plugins/printercounters/LICENSE', 'PrinterCounters', 'https://plugins.glpi-project.org/#/plugin/printercounters', 'PluginPrinterCounters'],
           ['/plugins/processmaker/processmaker.xml', 'Processmaker', 'https://plugins.glpi-project.org/#/plugin/processmaker', 'PluginProcessmaker'],
           ['/plugins/seasonality/README.md', 'Seasonality', 'https://plugins.glpi-project.org/#/plugin/seasonality', 'PluginSeasonality'],
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
           ['/plugins/officeonline/js/officeonline.js', 'Office Online', 'https://plugins.glpi-project.org/#/plugin/officeonline', 'PluginOfficeOnline'],
           ['/plugins/satisfaction/satisfaction.js', 'More satisfaction', 'https://plugins.glpi-project.org/#/plugin/satisfaction', 'PluginMoreSatisfaction'],
           ['/plugins/gdrive/README.md', 'GDrive', 'https://plugins.glpi-project.org/#/plugin/GDrive', 'PluginGDrive'],
           ['/plugins/archisw/archisw.xml', 'Apps structure inventory', 'https://plugins.glpi-project.org/#/plugin/archisw', 'PluginAppsStructureInventory'],
           ['/plugins/dataflows/dataflows.xml', 'Dataflows inventory', 'https://plugins.glpi-project.org/#/plugin/dataflows', 'PluginDataflowsInventory'],
           ['/plugins/statecheck/statecheck.xml', 'Statecheck', 'https://plugins.glpi-project.org/#/plugin/statecheck', 'PluginStatecheck'],
           ['/plugins/archimap/archimap.xml', 'Diagrams', 'https://plugins.glpi-project.org/#/plugin/archimap', 'PluginDiagrams'],
           ['/plugins/metabase/metabase.xml', 'Metabase', 'https://plugins.glpi-project.org/#/plugin/metabase', 'PluginMetabase'],
           ['/plugins/orderservice/orderservice.xml', 'Order Service', 'https://plugins.glpi-project.org/#/plugin/orderservice', 'PluginOrderService'],
           ['/plugins/glpicheckingversion/glpicheckingversion.xml', 'GLPI Checking Version', 'https://plugins.glpi-project.org/#/plugin/glpicheckingversion', 'PluginGLPICheckingVersion'],
           ['/plugins/taskdrop/LICENSE', 'Task n Drop', 'https://plugins.glpi-project.org/#/plugin/TaskDrop', 'PluginTaskDrop'],
           ['/plugins/impacts/impacts.xml', 'Impacts', 'https://plugins.glpi-project.org/#/plugin/impacts', 'PluginImpacts'],
           ['/plugins/manufacturersimports/LICENSE', 'Manufacturers Web Imports', 'https://plugins.glpi-project.org/#/plugin/manufacturersimports', 'PluginManufacturersImports'],
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
       ['GLPI', [['>=', '9.2.0'], ['<', '9.3.0']], 'SQL injection in front/computer.php', 'https://github.com/glpi-project/glpi/issues/4270', 'CVE-2018-13049'],
       ['GLPI', [['<=', '9.2.1']], 'Remote code execution' ,'https://github.com/bowline90/RemoteCodeUploadGLPI', 'CVE-2018-7562'],
       ['GLPI', [['=', '9.3.1']], 'Cross Site Scripting (XSS) in /glpi/ajax/getDropDownValue.php' ,'https://nvd.nist.gov/vuln/detail/CVE-2019-1010307', 'CVE-2019-1010307'],
       ['GLPI', [['=', '9.3.1']], 'Frame and Form tags Injection' ,'https://nvd.nist.gov/vuln/detail/CVE-2019-1010310', 'CVE-2019-1010310'],
       ['GLPI', [['<=', '9.3.3']], 'Pre-authenticated SQL injection' ,'https://www.synacktiv.com/ressources/advisories/GLPI_9.3.3_SQL_Injection.pdf', 'CVE-2019-10232'],
       ['GLPI', [['>=', '9.3'], ['<', '9.3.4']], 'Type juggling authentication bypass', 'https://www.synacktiv.com/ressources/GLPI_9.4.0_Type_juggling_auth_bypass.pdf', 'CVE-2019-10231'],
       ['GLPI', [['>=', '9.4'], ['<', '9.4.1.1']], 'Type juggling authentication bypass', 'https://www.synacktiv.com/ressources/GLPI_9.4.0_Type_juggling_auth_bypass.pdf', 'CVE-2019-10231'],
       ['GLPI', [['>=', '9.3'], ['<', '9.3.4']], 'Timing attack user enumeration', 'https://www.synacktiv.com/ressources/GLPI_9.4.0_Timing_attack_user_enumeration.pdf', 'CVE-2019-10233'],
       ['GLPI', [['>=', '9.4'], ['<', '9.4.1.1']], 'Timing attack user enumeration', 'https://www.synacktiv.com/ressources/GLPI_9.4.0_Timing_attack_user_enumeration.pdf', 'CVE-2019-10233'],
       ['GLPI', [['>=', '9'], ['<', '9.4.1']], 'Unsafe password reset' ,'https://www.synacktiv.com/ressources/advisories/GLPI_9.4.0_unsafe_reset.pdf', 'CVE-2019-13240'],
       ['GLPI', [['>=', '9'], ['<', '9.4.3']], 'Cross Site Scripting in inc/user.class.php via a user picture' ,'https://www.synacktiv.com/ressources/advisories/GLPI_9.4.0_stored_XSS.pdf', 'CVE-2019-13239'],
       ['FusionInventory', [['>=', '9.3'], ['<', '9.3+1.4']], 'Arbitrary PHP function call', 'https://www.synacktiv.com/ressources/GLPI_FusionInventory_9.4.0_Arbitrary_call_user_func_array.pdf', 'CVE-2019-10477'],
       ['FusionInventory', [['>=', '9.4'], ['<', '9.4+1.1']], 'Arbitrary PHP function call', 'https://www.synacktiv.com/ressources/GLPI_FusionInventory_9.4.0_Arbitrary_call_user_func_array.pdf', 'CVE-2019-10477'],
       ['Fields', [['<=', '1.9.2']], 'Unauthenticated SQL Injection ajax/reorder.php via container_id and old_order parameters', 'https://github.com/pluginsGLPI/fields/pull/317', 'CVE-2019-12723'],
       ['News', [['<=', '1.5.2']], 'Stored Cross Site Scripting in /front/alert.form.php via $_POST[\'name\'] parameter', 'https://github.com/pluginsGLPI/news/pull/69', 'CVE-2019-12724'],
       ['Dashboard', [['<=', '0.9.7']], 'Incorrect access control /front/sh/df.php, /front/sh/issue.php, /front/sh/load.php, /front/sh/mem.php, /front/sh/traf.php, and /front/sh/uptime.php', 'https://github.com/stdonato/glpi-dashboard/commit/3a89f0085a221d7ad76d1104df6df6c634bd7f14', 'CVE-2019-12530'],
       ['GLPI', [['<', '9.4.3']], 'Account takeover', 'https://www.tarlogic.com/advisories/Tarlogic-2019-GPLI-Account-Takeover.txt', 'CVE-2019-14666'],
       ['GLPI', [['>=', '0.78'], ['<=', '9.4.5']], 'GZIP RCE', 'https://github.com/AlmondOffSec/PoCs/blob/master/glpi_rce_gzip/poc.txt', 'CVE-2020-11060'],
       ['GLPI', [['>=', '0.80'], ['<=', '9.4.5']], 'GLPI static encryption key', 'https://offsec.almond.consulting/multiple-vulnerabilities-in-glpi.html', 'CVE-2020-5248'],
       ['GLPI', [['>=', '0.90.1'], ['<=', '9.4.5']], 'Open Redirect', 'https://offsec.almond.consulting/multiple-vulnerabilities-in-glpi.html', 'CVE-2020-11034'],
       ['GLPI', [['<', '9.4.6']], 'Multiple XSS', 'https://offsec.almond.consulting/multiple-vulnerabilities-in-glpi.html', 'CVE-2020-11036'],
       ['GLPI', [['>=', '0.83.3'], ['<=', '9.4.5']], 'Weak CSRF tokens', 'https://offsec.almond.consulting/multiple-vulnerabilities-in-glpi.html', 'CVE-2020-11035'],
       ['GLPI', [['>', '0.68.1'], ['<=', '9.4.5']], 'Reflected XSS in Dropdown endpoints', 'https://offsec.almond.consulting/multiple-vulnerabilities-in-glpi.html', 'CVE-2020-11062'],
       ['GLPI', [['=', '9.4.5']], 'SQL injection on addme_observer and addme_assign', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-344w-34h9-wwhh', 'CVE-2020-11032'],
       ['GLPI', [['>', '9.1'], ['<', '9.4.6']], 'Able to read any token through API user endpoint', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-rf54-3r4w-4h55', 'CVE-2020-11033'],
       ['GLPI', [['>=', '0.68'], ['<', '9.5.2']], 'Multiple SQL Injections Stemming From isNameQuoted()', 'https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15176', 'CVE-2020-15176'],
       ['GLPI', [['>=', '0.70'],['<', '9.5.2']], 'Unauthenticated File Deletion', 'https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15175', 'CVE-2020-15175'],
       ['GLPI', [['>=', '9.5.0'], ['<', '9.5.2']], 'User information leakage in Public FAQ', 'https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15217', 'CVE-2020-15217'],
       ['GLPI', [['>=', '0.65'], ['<', '9.5.2']], 'Unauthenticated Cross Site Scripting (XSS) in install/install.php', 'https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15177', 'CVE-2020-15177'],
       ['GLPI', [['>', '9.1'],['<', '9.5.2']], 'SQL Injection in the APIs search function', 'https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15226', 'CVE-2020-15226'],
       ['GLPI', [['<', '9.5.3']], 'Authenticated insecure direct object reference on ajax/getDropdownValue.php', 'https://cve.mitre.org/cgi-bin/cvename.cgi?name=2020-27663', 'CVE-2020-27663'],
       ['GLPI', [['<', '9.5.3']], 'Authenticated insecure direct object reference on ajax/comments.php', 'https://cve.mitre.org/cgi-bin/cvename.cgi?name=2020-27662', 'CVE-2020-27662'],
       ['GLPI', [['=', '9.5.0']], 'Authenticated read of any CalDAV calendars', 'https://cve.mitre.org/cgi-bin/cvename.cgi?name=2020-26212', 'CVE-2020-26212'],
       ['GLPI', [['=', '9.5.0']], 'SQL injection for all usage of "Clone" feature.', 'https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-15108', 'CVE-2020-15108'],
       ['GLPI', [['<', '9.5.4']], 'Unsafe Reflection in getItemForItemtype()', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-qmw7-w2m4-rjwp', 'CVE-2021-21327'],
       ['GLPI', [['<=', '9.5.3']], 'Horizontal Privilege Escalation', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-vmj9-cg56-p7wh', 'CVE-2021-21326'],
       ['GLPI', [['<', '9.5.4']], 'Stored XSS in budget type', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-m574-f3jw-pwrf', 'CVE-2021-21325'],
       ['GLPI', [['<', '9.5.4']], 'Insecure Direct Object Reference', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-jvwm-gq36-3v7v', 'CVE-2021-21324'],
       ['GLPI', [['<', '9.5.4']], 'XSS injection on ticket update', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-2w7j-xgj7-3xgg', 'CVE-2021-21314'],
       ['GLPI', [['<', '9.5.4']], 'XSS on tabs', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-h4hj-mrpg-xfgx', 'CVE-2021-21313'],
       ['GLPI', [['<', '9.5.4']], 'Stored XSS on documents', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-c7f6-3mr7-3rq2', 'CVE-2021-21312'],
       ['GLPI', [['>=', '9.5.0'], ['<', '9.5.4']], 'XSS injection in ajax/kanban', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-j4xj-4qmc-mmmx', 'CVE-2021-21258'],
       ['GLPI', [['=', '9.5.3']], 'Entities switch IDOR', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-v3m5-r3mx-ff9j', 'CVE-2021-21255'],
       ['GLPI', [['<', '9.5.5']], 'Stored Cross-Site Scripting (XSS)', 'https://n3k00n3.github.io/blog/09042021/glpi_xss.html', 'CVE-2021-3486'],
       ['GLPI', [['<', '9.5.6']], 'CSRF Bypass', 'https://github.com/glpi-project/glpi/releases/tag/9.5.6', 'CVE-2021-39209'],
       ['GLPI', [['<', '9.5.6']], 'Autologin cookie accessible by scripts', 'https://github.com/glpi-project/glpi/releases/tag/9.5.6', 'CVE-2021-39210'],
       ['GLPI', [['>=', '9.2'], ['<', '9.5.6']], 'Disclosure of GLPI and server informations in telemetry endpoint', 'https://github.com/glpi-project/glpi/releases/tag/9.5.6', 'CVE-2021-39211'],
       ['GLPI', [['>=', '9.1'],['<', '9.5.6']], 'Bypassable IP restriction on GLPI API using custom header injection', 'https://github.com/glpi-project/glpi/releases/tag/9.5.6', 'CVE-2021-39213'],
       ['Ramo', [['=', '9.4.6']], 'SQL Injection in Ramo Plugin', 'https://packetstormsecurity.com/files/166285/Baixar-GLPI-Project-9.4.6-SQL-Injection.html', 'CVE-2021-44617'],
       ['GLPI', [['<', '9.5.7']], 'SQL injection using custom CSS administration form', 'https://github.com/glpi-project/glpi/commit/5c3eee696b503fdf502f506b00d15cf5b324b326', 'CVE-2022-21720'],
       ['GLPI', [['<=', '9.5.7']], 'Reflected XSS using reload button', 'https://github.com/glpi-project/glpi/commit/e9b16bc8e9b61ebb2d35b96b9c71cd25c5af9e48', 'CVE-2022-21719'],
       ['GLPI', [['<', '10.0.0']], 'LDAP password exposed on source code', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-4r49-52q9-5fgr', 'CVE-2022-24867'],
       ['GLPI', [['>=', '0.90'],['<', '10.0.0']], 'Cross Site CSS Injection', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-p94c-8qp5-gfpx', 'CVE-2022-24869'],
       ['GLPI', [['<', '10.0.0']], 'XSS / open redirect via SVG file upload', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-9hg4-fpwv-gx78', 'CVE-2022-24868'],
       ['GLPI', [['=', '10.0.0'],['<', '10.0.1']], 'Stored XSS on Kanban', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-33g2-m556-gccr', 'CVE-2022-24876'],
       ['GLPI', [['=', '10.0.0'],['<', '10.0.1']], 'SQL injection on search pages', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-5w33-4wrx-8hvw', 'CVE-2022-29250'],
       ['GLPI', [['=', '10.0.0'],['<', '10.0.2']], 'SQL injection on login page', 'https://www.swascan.com/security-advisory-teclib-glpi/', 'CVE-2022-31061'],
       ['GLPI', [['<', '9.5.8']], 'SQL injection on login page', 'https://www.swascan.com/security-advisory-teclib-glpi/', 'CVE-2022-31061'],
       ['GLPI', [['>=', '10.0.0'],['<', '10.0.2']], 'SQL injection with _actor parameter in assistance objects', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-9q9x-7xxh-w4cg', 'CVE-2022-31056'],
       ['GLPI', [['>=', '10.0.0'],['<', '10.0.2']], 'Unauthenticated Sensitive Data Exposure on Refused Inventory Files', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-g4hm-6vfr-q3wg', 'CVE-2022-31068'],
       ['GLPI', [['>=', '9.5.0'],['<', '10.0.3']], 'XSS through registration API', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-jrgw-cx24-56x5', 'CVE-2022-35945'],
       ['GLPI', [['>=', '9.5.0'],['<','10.0.3']], 'Leak of sensitive informations through login page error', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-6mmq-x3j2-677j', 'CVE-2022-31143'],
       ['GLPI', [['=', '10.0.0'],['<', '10.0.3']], 'Stored XSS through global search', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-43j5-xhvj-9236', 'CVE-2022-31187'],
       ['GLPI', [['<', '10.0.0'],['<', '10.0.3']], 'Command injection using a third-party library script', 'https://mayfly277.github.io/posts/GLPI-htmlawed-CVE-2022-35914/', 'CVE-2022-35914'],
       ['GLPI', [['<', '9.5.4']], 'Command injection using a third-party library script', 'https://mayfly277.github.io/posts/GLPI-htmlawed-CVE-2022-35914/', 'CVE-2022-35914'],
       ['GLPI', [['>=', '0.72'],['<', '10.0.3']], 'SQL injection through plugin controller', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-92q5-pfr8-r9r2', 'CVE-2022-35946'],
       ['GLPI', [['>=', '10.0.0'],['<', '10.0.03']], 'Authentication via SQL injection', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-7p3q-cffg-c8xh', 'CVE-2022-35947'],
       ['GLPI', [['<', '9.5.9']], 'Authentication via SQL injection', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-7p3q-cffg-c8xh', 'CVE-2022-35947'],
       ['GLPI', [['>=', '10.0.0'],['<', '10.0.3']], 'Blind Server-Side Request Forgery (SSRF) in RSS feeds and planning', 'https://huntr.dev/bounties/a0788aa8-212f-4624-9086-8b7f391dddac/', 'CVE-2022-36112'],
       ['GLPI', [['>=', '0.70'],['<', '10.0.4']], 'Improper access to debug panel', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-6c2p-wgx9-vrjc', 'CVE-2022-39370'],
       ['GLPI', [['<', '10.0.4']], 'User\'s session persist after permanently deleting his account', 'https://huntr.dev/bounties/62096b15-2b7b-4de3-96d1-32754c5f9d44/', 'CVE-2022-39234'],
       ['GLPI', [['>=', '0.65'],['<', '10.0.4']], 'Stored XSS on login page', 'https://huntr.dev/bounties/54fc907e-6983-4c24-b249-1440aac1643c/', 'CVE-2022-39262'],
       ['GLPI', [['>=', '9.1'],['<', '10.0.4']], 'SQL Injection on REST API', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-cp6q-9p4x-8hr9', 'CVE-2022-39323'],     
       ['GLPI', [['<', '10.0.4']], 'Blind Server-Side Request Forgery (SSRF) in RSS feeds and planning', 'https://huntr.dev/bounties/7a88f92b-1ee2-4ca8-9cf8-05fcf6cfe73f/', 'CVE-2022-39276'],     
       ['GLPI', [['>=', '0.60'],['<', '10.0.4']], 'XSS in external links', 'https://huntr.dev/bounties/8e047ae1-7a7c-48e0-bee3-d1c36e52ff42/', 'CVE-2022-39277'],     
       ['GLPI', [['>=', '0.70'],['<', '10.0.4']], 'Stored XSS in user information', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-5rj7-95qc-89h2', 'CVE-2022-39372'],     
       ['GLPI', [['>=', '10.0.0'],['<', '10.0.4']], 'Stored XSS through asset inventory', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-w7wc-728f-6mm8', 'CVE-2022-39371'],     
       ['GLPI', [['>= ', '10.0.0'],['<', '10.0.4']], 'Stored XSS in entity name', 'https://huntr.dev/bounties/d3c269fc-a865-425f-89e1-15fb32e85e96/', 'CVE-2022-39373'],     
       ['GLPI', [['>=', '0.84'],['<', '10.0.4']], 'XSS through public RSS feed', 'https://huntr.dev/bounties/b45146ef-0f1a-4de9-90be-5c4d78b34fdf/', 'CVE-2022-39375'],     
       ['GLPI', [['>=', '10.0.0'],['<', '10.0.6']], 'Improper input validation on emails links', 'https://huntr.dev/bounties/3557ccc4-9325-41e8-ae01-18685adcd888/', 'CVE-2022-39376'],     
       ['GLPI', [['>=', '0.70'],['<', '9.5.12']], 'Improper input validation on emails links', 'https://huntr.dev/bounties/3557ccc4-9325-41e8-ae01-18685adcd888/', 'CVE-2022-39376'],     
       ['GLPI', [['>=', '10.0.0'],['<', '10.0.6']], 'XSS Stored inside Standard Interface Help Link href attribute', 'https://huntr.dev/bounties/67f2f5da-5316-4bae-96b6-b0f0d719c4bf/', 'CVE-2022-41941'],     
       ['GLPI', [['>=', '0.70'],['<', '9.5.12']], 'XSS Stored inside Standard Interface Help Link href attribute', 'https://huntr.dev/bounties/67f2f5da-5316-4bae-96b6-b0f0d719c4bf/', 'CVE-2022-41941'],     
       ['GLPI', [['>=', '10.0.0'],['<', '10.0.6']], 'XSS in RSS Description Link', 'https://huntr.dev/bounties/dda8bb6d-c556-4a21-9308-43c5bf968003/', 'CVE-2023-22724'],     
       ['GLPI', [['>=', '0.60'],['<', '9.5.12']], 'XSS on external links', 'https://huntr.dev/bounties/9976a2ed-b105-453c-8af8-2768eb1bbb87/', 'CVE-2023-22725'],     
       ['GLPI', [['>=', '10.0.0'],['<', '10.0.6']], 'XSS on external links', 'https://huntr.dev/bounties/9976a2ed-b105-453c-8af8-2768eb1bbb87/', 'CVE-2023-22725'],     
       ['GLPI', [['>=', '9.4.0'],['<', '9.5.12']], 'XSS on browse views', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-352j-wr38-493c', 'CVE-2023-22722'],     
       ['GLPI', [['>=', '10.0.0'],['<', '10.0.6']], 'XSS on browse views', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-352j-wr38-493c', 'CVE-2023-22722'],     
       ['GLPI', [['>=', '10.0.0'],['<', '10.0.6']], 'Unauthorized access to inventory files', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-3ghv-p34r-5ghx', 'CVE-2023-22500'],     
       ['GLPI', [['>=', '10.0.0'],['<', '10.0.6']], 'Unauthorized access to data export', 'https://github.com/glpi-project/glpi/security/advisories/GHSA-6565-hm87-24hf', 'CVE-2023-23610'], 
       ]
