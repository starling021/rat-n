import time
import json
import modules.helper as h

class command:
    def __init__(self):
        self.name = "icons"
        self.description = "List macOS alert icons."
        self.type = "applescript"

    def run(self,session,cmd_data):
        print("""
    
