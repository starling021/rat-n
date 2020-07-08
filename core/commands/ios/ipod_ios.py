#!/usr/bin/env python3

import core.helper as h

class command:
    def __init__(self):
        self.name = "ipod"
        self.description = "Control music player."
        self.usage = "Usage: ipod [play|pause|next|prev|info]"
    
    def run(self,session,cmd_data):
        if not cmd_data['args'] or not cmd_data['args'] in ['play','pause','next','prev','info']:
            print(self.usage)
        result = session.send_command(cmd_data)
        if result:
            if result.decode().rstrip() == "Not Playing":
                h.info_error("Not playing!")
            else:
                print(result.decode().rstrip())
