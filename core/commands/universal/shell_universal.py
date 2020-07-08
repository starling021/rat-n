#!/usr/bin/env python3

import core.helper as h
import time
import json
import os

class command:
	def __init__(self):
		self.name = "shell"
		self.description = "Open device shell."

	def run(self,session,cmd_data):
		h.info_general("Connecting to device...")
		time.sleep(0.5)
		h.info_general("Opening device shell...")
		time.sleep(1)
		while 1:
			uid = session.send_command({"cmd":"echo","args":"$UID"}).decode()
			if uid[:-1] == "0":
				whoami = "# "
			else:
				whoami = "$ "
			shell = input(h.ENDC+session.hostname+":"+session.current_directory+" "+session.username+whoami).strip(" ")
			if not shell or shell.replace(" ","") == "":
				continue
			shelld = shell.split()[0]
			shelld_data = {"cmd": shelld, "args":shell[len(shelld) + 1:]}
			if shelld == "cd":
				result = json.loads(session.send_command(shelld_data))
				if 'error' in result:
					h.info_error(result['error'])
				elif 'current_directory' in result:
					session.current_directory = result['current_directory']
				else:
					h.info_error('Unable to get current directory!')
			if shelld == "ls":
				if len(shell.split()) < 2:
					print(session.send_command({'cmd':'ls -al','args':'.'}).decode())
				else:
					print(session.send_command({'cmd':'ls -al','args':shell.split()[1]}).decode())
			if shelld == "exit":
				return
			else:
				try:
					if shelld == "ls" or shelld == "cd":
						pass
					else:
						result = session.send_command({'cmd':'','args':shell})
						if result:
							print(result.decode().rstrip())
				except KeyboardInterrupt:
					session.send_command({"cmd":"killtask"})
