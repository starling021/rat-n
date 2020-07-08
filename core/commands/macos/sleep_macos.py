#!/usr/bin/env python3

import core.helper as h

class command:
    def __init__(self):
        self.name = "sleep"
        self.description = "Put device into sleep mode."

    def run(self,session,cmd_data):
        cmd_data["cmd"] = "osascript"
        cmd_data["args"] = " -e 'tell application \"Finder\" to sleep'"
        error = session.send_command(cmd_data)
        if error:
            h.info_error("Failed to put device into sleep mode!")