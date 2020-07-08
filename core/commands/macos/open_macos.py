#!/usr/bin/env python3

import time
import json
import core.helper as h

class command:
    def __init__(self):
        self.name = "open"
        self.description = "Open application."

    def run(self,session,cmd_data):
        one = '"'
        if cmd_data['args'] == "":
            print("Usage: open <application>")
        cmd_data.update({"cmd":"osascript","args":"-e 'tell application "+one+""+cmd_data['args']+""+one+" to activate'"})
        app = session.send_command(cmd_data).strip()
        return ""
