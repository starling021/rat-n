#!/usr/bin/env python3

import core.helper as h

class command:
    def __init__(self):
        self.name = "volume"
        self.description = "Show volume level."
    
    def run(self,session,cmd_data):
        cmd_data = {'cmd': 'getvol', 'args': ''}
        h.info_info("Volume level: "+session.send_command(cmd_data).decode())
