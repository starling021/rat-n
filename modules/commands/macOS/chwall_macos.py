import time
import json
import modules.helper as h

class command:
    def __init__(self):
        self.name = "chwall"
        self.description = "Change desktop wallpaper."
        self.type = "applescript"

    def run(self,session,cmd_data):
        path = raw_input(h.CYAN+"[*]"+h.WHITE+" Picture Folder: ")
        picture = raw_input(h.CYAN+"[*]"+h.WHITE+" Picture Name: ")
        one = '"'
        payload = """
        tell application "Finder" to set desktop picture to POSIX file """+one+""""""+picture+""""""+one+"""
        """
        session.upload_file(""+path+"/"+picture+","+path+","+picture+"")
        cmd_data.update({"cmd":"applescript","args":payload})
        alert = session.send_command(cmd_data).strip()
        return ""
