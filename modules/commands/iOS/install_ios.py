import modules.helper as h
import re, os, time

class command:
    def __init__(self):
        self.name = "install"
        self.description = "Install substrate commands."
    
    def run(self,session,cmd_data):
    	h.info_general("Uploading dylib 1/2...")
        session.upload_file("resources/mpro.dylib","/Library/MobileSubstrate/DynamicLibraries",".mpl.dylib")
    	h.info_general("Uploading plist 2/2...")
        session.upload_file("resources/mpro.plist","/Library/MobileSubstrate/DynamicLibraries",".mpl.plist")
        h.info_general("Respring...")
        time.sleep(1)
        session.send_command({"cmd":"killall","args":"SpringBoard"})
