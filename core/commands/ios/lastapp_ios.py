#!/usr/bin/env python3

import core.helper as h

class command:
    def __init__(self):
        self.name = "lastapp"
        self.description = "Show last opened application."
    
    def run(self,session,cmd_data):
        h.info_info("Last application: " + session.send_command(cmd_data).decode())
