import time
import json
import modules.helper as h

class command:
    def __init__(self):
        self.name = "close"
        self.description = "Close application."

    def run(self,session,cmd_data):
        one = '"'
        if cmd_data['args'] == "":
            print("Usage: close <application>")
        cmd_data.update({"cmd":"osascript","args":"-e 'quit app "+one+""+cmd_data['args']+""+one+"'"})
        app = session.send_command(cmd_data).strip()
        return ""
