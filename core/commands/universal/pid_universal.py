#!/usr/bin/env python3

import core.helper as h

class command:
    def __init__(self):
        self.name = "pid"
        self.description = "Show Mouse process ID."
        self.type = "native"

    def run(self,session,cmd_data):
        h.info_info("PID: "+session.send_command(cmd_data).decode())
