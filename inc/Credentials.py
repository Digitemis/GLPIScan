#!/usr/bin/python

import Config

import requests, chalk

class CredentialsCheck:

	def getLoginField(self, content):
		login = content[content.find('<input type="text" name="')+len('<input type="text" name="'):]
		login = login[:login.find('"')]
		return login

	def getPasswordField(self, content):
		password = content[content.find('<input type="password" name="')+len('<input type="password" name="'):]
		password = password[:password.find('"')]
		return password

	def getCSRFField(self, content):
		csrf = content[content.find('_glpi_csrf_token" value="')+len('_glpi_csrf_token" value="'):]
		csrf = csrf[:csrf.find('"')]
		return csrf

	def Authenticate(self, user, loginField, passwordField, CSRFField):
		payload = {'noAUTO': '1', loginField: user[0], passwordField: user[1], 'auth': 'local', 'submit': 'Envoyer', '_glpi_csrf_token': CSRFField}
		cookie = {Config.COOKIE.split('=')[0]:Config.COOKIE.split('=')[1]}
		if Config.DEBUG:
			print("[DEBUG] POST : " + Config.BASE_URL + "/front/login.php")
		proxy = {"http": "http://127.0.0.1:8080"}
		r = requests.post(Config.BASE_URL + "/front/login.php", data=payload, cookies=cookie, allow_redirects=False, verify=False)
		if r.status_code == 302:
			print(chalk.white('[+] Valid user account found : ', bold=True) + chalk.red(user[0] + ':' + user[1], bold=True))

	def getAuthForm(self, user):
		if Config.DEBUG:
			print("[DEBUG] GET : " + Config.BASE_URL)
		r = requests.get(Config.BASE_URL, verify=False)
		Config.COOKIE = r.headers.get('Set-Cookie').split(';')[0]
		loginField = self.getLoginField(r.content)
		passwordField = self.getPasswordField(r.content)
		CSRFField = self.getCSRFField(r.content)
		self.Authenticate(user, loginField, passwordField, CSRFField)

	def credentials(self):
		print(chalk.green('\n[+] Performing Credential check', bold=True))
		print(chalk.green('===============================\n', bold=True))
		for user in Config.USERS:
			if Config.DEBUG:
				print("[DEBUG] Trying " + user[0] + ":" + user[1])
			self.getAuthForm(user)