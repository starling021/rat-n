#!/usr/bin/env python3



import core.helper as h

class command:
    def __init__(self):
        self.name = "battery"
        self.description = "Show battery level."
    
    def run(self,session,cmd_data):
        h.info_info("Battery level: " + session.send_command(cmd_data).decode()[15:])
