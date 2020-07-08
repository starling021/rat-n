#!/usr/bin/env python3

class command:
    def __init__(self):
        self.name = "setbright"
        self.description = "Set screen brightness."
        self.usage = "Usage: setbrigh <level: 0-1>"
        self.type = "native"
    
    def run(self,session,cmd_data):
        try:
            float(cmd_data["args"])
        except:
            print(self.usage)
            return
        session.send_command(cmd_data)
