#!/usr/bin/env python3

import core.helper as h

class command:
    def __init__(self):
        self.name = "setvol"
        self.description = "Set output volume."
     
    def run(self,session,cmd_data):
        if not cmd_data['args']:
            print("Usage: setvol <level: 0-100>")
            return -1
        payload = "set volume output volume "+cmd_data['args']
        cmd_data.update({"cmd":"applescript","args":payload})
        error = session.send_command(cmd_data)
        if error:
            h.info_error("Failed to set output volume!")
