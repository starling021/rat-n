import time
import json
import os
import modules.helper as h

class command:
    def __init__(self):
        self.name = "syscmds"
        self.description = "Display all system commands."

    def run(self,session,cmd_data):
        print h.WHITEBU+"System Commands:"+h.ENDC
        cmd_data({"cmd":"compgen","args":"-c | sort"})
