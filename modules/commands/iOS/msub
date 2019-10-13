import modules.helper as h
import re, os, time

class command:
    def __init__(self):
        self.name = "msub"
        self.description = "Install MPL Substrate."
    
    def run(self,session,cmd_data):
    	h.info_general("Uploading dylib 1/2...")
        session.upload_file("substrate/mpl.dylib","/Library/MobileSubstrate/DynamicLibraries",".mpl.dylib")
    	h.info_general("Uploading plist 2/2...")
        session.upload_file("substrate/mpl.plist","/Library/MobileSubstrate/DynamicLibraries",".mpl.plist")
        h.info_general("Restarting SpringBoard...")
        time.sleep(1)
session.send_command({"cmd":"killall","args":"SpringBoard"})
