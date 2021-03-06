#!/usr/bin/env python3

import core.helper as h
import time
import base64
import json
try:
    # Win32
    from msvcrt import getch
except ImportError:
    # UNIX
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

class command:
    def __init__(self):
        self.name = "keyboard"
        self.description = "Control device keyboard."
        self.type = "applescript"
        self.id = 115

    def run(self,session,cmd_data):
        h.info_info("Press Ctrl-C to stop.")
        h.info_info("Device keyboard:")
        while 1:
            key = getch()
            if key == chr(3):
                return ""
            payload = """tell application "System Events"
            keystroke \""""+key+"""\"
            end tell"""
            session.send_command({"cmd":"applescript","args":payload})
        return ""

