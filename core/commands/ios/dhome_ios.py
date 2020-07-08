#!/usr/bin/env python3

import core.helper as h

class command:
    def __init__(self):
        self.name = "dhome"
        self.description = "Simulate a double home button press."
    
    def run(self,session,cmd_data):
        cmd_data["cmd"] = "doublehome"
        error = session.send_command(cmd_data)
        if error:
            h.info_error("Mouse Substrate is not installed!")
