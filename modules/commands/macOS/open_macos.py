import time
import json
import modules.helper as h

class command:
    def __init__(self):
        self.name = "open"
        self.description = "Make alert show up on device."
        self.type = "applescript"

    def run(self,session,cmd_data):
        one = '"'
        cmd_data.update({"cmd":"osascript","args":"-e 'tell application "+one+""+cmd_data['args']+""+one+" to activate'"})
        alert = session.send_command(cmd_data).strip()
        return ""
