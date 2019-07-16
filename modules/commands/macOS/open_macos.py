import time
import json
import modules.helper as h

class command:
    def __init__(self):
        self.name = "open"
        self.description = "Open application."
        self.usage = "Usage: open <application>"

    def run(self,session,cmd_data):
        one = '"'
        if cmd_data['args'] == "":
            print("Usage: close <application>")
        cmd_data.update({"cmd":"osascript","args":"-e 'tell application "+one+""+cmd_data['args']+""+one+" to activate'"})
        app = session.send_command(cmd_data).strip()
        return ""
