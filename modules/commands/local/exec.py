import os
from os.path import expanduser
import modules.helper as h

class command:
    def __init__(self):
        self.name = "exec"
        self.description = "Execute local shell commands."
    
    def run(self,session,cmd_data):
        if not cmd_data['args']:
            print "Usage: local <command>"
            return
        else:
            print(h.CYAN+"[*]"+h.WHITE+" Exec: "+cmd_data['args'])
            split_args = cmd_data['args'].split()
            if split_args[0] == "cd":
                path = cmd_data['args'][2:].strip()
                if not path:
                    path = expanduser("~")
                os.chdir(path)
            else:
            	os.system(cmd_data['args'])

