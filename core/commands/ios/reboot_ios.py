#!/usr/bin/env python3

import core.helper as h
import time

class command:
	def __init__(self):
		self.name = "reboot"
		self.description = "Reboot device."

	def run(self,session,cmd_data):
		h.info_general("Rebooting device...")
		time.sleep(1)
		session.send_command({"cmd":"reboot","args":""})
