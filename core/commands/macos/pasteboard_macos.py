#!/usr/bin/env python3

import core.helper as h

class command:
    def __init__(self):
        self.name = "pasteboard"
        self.description = "Show pasteboard contents."
        self.type = "native"

    def run(self,session,cmd_data):
        h.info_info("Pasteboard contents:")
        print(session.send_command(cmd_data).decode())
