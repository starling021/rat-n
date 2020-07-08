#!/usr/bin/env python3



import core.helper as h

class command:
    def __init__(self):
        self.name = "apps"
        self.description = "List all applications."
    
    def run(self,session,cmd_data):
        cmd_data = {'cmd': 'bundleids', 'args': ''}
        print(session.send_command(cmd_data).decode().rstrip())
