import modules.helper as h
import re, os, time

class command:
    def __init__(self):
        self.name = "install"
        self.description = "Install Mouse Substrate."
    
    def run(self,session,cmd_data):
    	h.info_general("Uploading dylib 1/2...")
        time.sleep(1)
        session.upload_file("resources/mpl.dylib","/Library/MobileSubstrate/DynamicLibraries",".mpl.dylib")
    	h.info_general("Uploading plist 2/2...")
        time.sleep(1)
        session.upload_file("resources/mpl.plist","/Library/MobileSubstrate/DynamicLibraries",".mpl.plist")
        h.info_general("Respring...")
        time.sleep(2)
        session.send_command({"cmd":"killall","args":"SpringBoard"})
