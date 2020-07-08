#!/usr/bin/env python3

class command:
	def __init__(self):
		self.name = "vibrate"
		self.description = "Vibrate device."

	def run(self,session,cmd_data):
		session.send_command(cmd_data)
