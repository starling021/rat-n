#!/usr/bin/env python3

class command:
	def __init__(self):
		self.name = "openurl"
		self.description = "Open URL on device."
		self.usage = "Usage: openurl <url>"

	def run(self,session,cmd_data):
		if not cmd_data['args']:
			print(self.usage)
			return
		session.send_command(cmd_data)
