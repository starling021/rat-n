#!/usr/bin/env python3

import core.helper as h
import time

class command:
	def __init__(self):
		self.name = "say"
		self.description = "Convert text to speach."
		self.usage = "Usage: say <text>"

	def run(self,session,cmd_data):
		if not cmd_data['args']:
			print(self.usage)
		else:
			session.send_command({"cmd":"say","args":cmd_data['args']})
