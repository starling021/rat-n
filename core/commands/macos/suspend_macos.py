#!/usr/bin/env python3

import core.helper as h

class command:
    def __init__(self):
        self.name = "suspend"
        self.description = "Suspend current session."

    def run(self,session,cmd_data):
        cmd_data["cmd"] = ";"
        cmd_data["args"] = '/System/Library/CoreServices/Menu\ Extras/User.menu/Contents/Resources/CGSession -suspend'
        error = session.send_command(cmd_data)
        if error:
            h.info_error("Failed to suspend current session!")
