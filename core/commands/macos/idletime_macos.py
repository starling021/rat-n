#!/usr/bin/env python3

import core.helper as h

class command:
    def __init__(self):
        self.name = "idletime"
        self.description = "Get the amount of user activity time."
        self.type = "native"

    def run(self,session,cmd_data):
        h.info_info("User has been idle for: "+session.send_command(cmd_data).decode())
