#!/usr/bin/env python3

import core.helper as h

class command:
    def __init__(self):
        self.name = "getpasscode"
        self.description = "Retreive the device passcode."
    
    def run(self,session,cmd_data):
        error = session.send_command(cmd_data)
        if error:
            h.info_error("Failed to retreive the device passcode!")
