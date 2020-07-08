#!/usr/bin/env python3

class command:
    def __init__(self):
        self.name = "setvol"
        self.description = "Set output volume."
        self.usage = "Usage: setvol <level: 0-1>"
    
    def run(self,session,cmd_data):
        if not cmd_data['args']:
            print(self.usage)
            return
        session.send_command(cmd_data)
