#!/usr/bin/env python3

import time
import json
import core.helper as h

class command:
    def __init__(self):
        self.name = "alert"
        self.description = "Make alert show up on device."
        self.usage = "Usage: <title> <message> <icon> <application> <first_button> <second_button>"
        self.type = "applescript"

    def run(self,session,cmd_data):
        cmds = cmd_data['args'].split()
        if len(cmds) < 6:
            print(self.usage)
        else:
            title = cmds[0]
            message = cmds[1]
            icon = cmds[2]
            application = cmds[3]
            fbutton = cmds[4]
            sbutton = cmds[5]
            one = '"'
            payload = """
            tell application """+one+""""""+application+""""""+one+"""
                activate
            
                set theAlertText to "An error has occurred."
                set theAlertMessage to "The amount of available free space is dangerously low. Would you like to continue?"
            
                    try
                        display dialog """+one+""""""+message+""""""+one+""" with title """+one+""""""+title+""""""+one+""" buttons {"""+one+""""""+fbutton+""""""+one+""", """+one+""""""+sbutton+""""""+one+"""} default button """+one+""""""+fbutton+""""""+one+""" cancel button """+one+""""""+sbutton+""""""+one+""" with icon path to resource """+one+""""""+icon+""".icns"""+one+""" in bundle "/System/Library/CoreServices/CoreTypes.bundle"
                    end try
                        
            end tell        
            """
            cmd_data.update({"cmd":"applescript","args":payload})
            alert = session.send_command(cmd_data).strip()
            return ""
