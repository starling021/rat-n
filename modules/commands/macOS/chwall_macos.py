import time
import json
import modules.helper as h

class command:
    def __init__(self):
        self.name = "chwall"
        self.description = "Change desktop wallpaper."
        self.type = "applescript"

        

    def run(self,session,cmd_data):
        picture = raw_input(h.CYAN+"[*]"+h.WHITE+" Wallpaper Picture: ")
        one = '"'
        payload = """
        tell application "Finder" to set desktop picture to POSIX file "picture.jpeg"
        """
        cmd_data.update({"cmd":"rm","args":"~/picture.jpeg"})
        session.upload_file(picture,"~","picture.jpeg")
        cmd_data.update({"cmd":"applescript","args":payload})
        alert = session.send_command(cmd_data).strip()
        return ""
