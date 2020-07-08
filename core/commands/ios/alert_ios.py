#!/usr/bin/env python3



import base64
import json
import core.helper as h

class command:
    def __init__(self):
        self.name = "alert"
        self.description = "Make alert show up on device."
        self.usage = "Usage: alert <title> <message>"
        self.type = "native"

    def run(self,session,cmd_data):
        cmds = cmd_data['args'].split()
        if len(cmds) < 2:
            print(self.usage)
        else:
            title = cmds[0]
            message = cmds[1]
            session.send_command({"cmd":"alert","args":json.dumps({"title":title,"message":message})})
            return ""
