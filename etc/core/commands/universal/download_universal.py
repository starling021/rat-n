#!/usr/bin/env python3

import json
import os
import core.helper as h
import re
import time

class command:
	def __init__(self):
		self.name = "download"
		self.description = "Download remote file."
		self.usage = "Usage: download <remote_file> <local_path>"
		self.type = "native"

	def run(self,session,cmd_data):
		if len(cmd_data['args'].split()) < 2:
			print(self.usage)
			return
		
		w = os.environ['OLDPWD']
		os.chdir(w)
		payload = """if [[ -d """+cmd_data['args'].split()[0]+""" ]]
		then
		echo 0
		fi"""
		dchk = session.send_command({"cmd":"","args":payload})
		chk = session.send_command({"cmd":"stat","args":cmd_data['args'].split()[0]})
		if chk[:4] != "stat":
			if dchk == "0\n":
				h.info_error("Error: "+cmd_data['args'].split()[0]+": not a file!")
			else:
				if os.path.isdir(cmd_data['args'].split()[1]):
					if os.path.exists(cmd_data['args'].split()[1]):
						rp = os.path.split(cmd_data['args'].split()[0])[1]
						data = session.download_file(cmd_data['args'].split()[0])
						h.info_general("Downloading {0}...".format(rp))
						if data:
							f = open(os.path.join(cmd_data['args'].split()[1],rp),'wb')
							f.write(data)
							f.close()
							if cmd_data['args'].split()[1][-1] == "/":
								h.info_general("Saving to " + cmd_data['args'].split()[1] + "" + rp + "...")
								time.sleep(1)
								h.info_success("Saved to " + cmd_data['args'].split()[1] + "" + rp + "!")
							else:
								h.info_general("Saving to " + cmd_data['args'].split()[1] + "/" + rp + "...")
								time.sleep(1)
								h.info_success("Saved to " + cmd_data['args'].split()[1] + "/" + rp + "!")
					else:
						h.info_error("Local directory: "+cmd_data['args'].split()[1]+": does not exist!")
				else:
					rp = os.path.split(cmd_data['args'].split()[1])[0]
					if rp == "":
						rp = "."
					else:
						pass
					if os.path.exists(rp):
						if os.path.isdir(rp):
							prr = os.path.split(cmd_data['args'].split()[1])[0]
							rp = os.path.split(cmd_data['args'].split()[1])[1]
							pr = os.path.split(cmd_data['args'].split()[0])[1]
							data = session.download_file(cmd_data['args'].split()[0])
							h.info_general("Downloading {0}...".format(pr))
							if data:
								h.info_general("Saving to {0}...".format(cmd_data['args'].split()[1]))
								f = open(os.path.join(prr,rp),'wb')
								f.write(data)
								f.close()
								h.info_success("Saved to "+cmd_data['args'].split()[1]+"!")
						else:
							h.info_error("Error: "+rp+": not a directory!")
					else:
						h.info_error("Local directory: "+rp+": does not exists!")
		else:
			h.info_error("Remote file: "+cmd_data['args'].split()[0]+": does not exist!")
		g = os.environ['HOME']
		os.chdir(g + "/mouse")
