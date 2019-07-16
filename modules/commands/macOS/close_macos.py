import time
import json
import modules.helper as h

class command:
    def __init__(self):
        self.name = "close"
        self.description = "Close application."
        self.usage = "Usage: close <application>"

    def run(self,session,cmd_data):
        one = '"'
        cmd_data.update({"cmd":"osascript","args":"-e 'quit app "+one+""+cmd_data['args']+""+one+"'"})
        app = session.send_command(cmd_data).strip()
        return ""
