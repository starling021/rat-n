#!/usr/bin/env python3

import json
import core.helper as h

class command:
    def __init__(self):
        self.name = "volume"
        self.description = "Show volume level."
        self.type = "applescript"

    def run(self,session,cmd_data):
        payload = "output volume of (get volume settings)"
        cmd_data.update({"cmd":"applescript","args":payload})
        h.info_info("Volume level: "+session.send_command(cmd_data).decode())
