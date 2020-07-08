#!/usr/bin/env python3

import core.helper as h

class command:
    def __init__(self):
        self.name = "open"
        self.description = "Open application."
        self.usage = "Usage: open <application>"
    
    def run(self,session,cmd_data):
        if not cmd_data['args']:
            print(self.usage)
        error = session.send_command(cmd_data)
        if error:
            h.info_error("Failed to open application!")
