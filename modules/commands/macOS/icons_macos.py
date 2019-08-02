import time
import json
import os
import modules.helper as h

class command:
    def __init__(self):
        self.name = "icons"
        self.description = "List system alert icons."

    def run(self,session,cmd_data):
                print(h.WHITEBU+"Alert Icons:"+h.ENDC)
        os.system("cd && cat mouse/resources/icons.txt")
