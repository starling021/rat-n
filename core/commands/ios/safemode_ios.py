#!/usr/bin/env python3

import core.helper as h
import time

class command:
    def __init__(self):
        self.name = "safemode"
        self.description = "Put device into SafeMode."

    def run(self,session,cmd_data):
        h.info_general("Launching SafeMode...")
        time.sleep(1)
        cmd_data["cmd"] = ";"
        cmd_data["args"] = "touch /var/mobile/Library/Preferences/com.saurik.mobilesubstrate.dat; killall SpringBoard"
        error = session.send_command(cmd_data)
        if error:
            h.info_error("Failed to put device into SafeMode!")
