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
        session.send_command({"cmd":"rm","args":"/var/picture.jpg"})
        session.upload_file(picture,"/var","picture.jpg")
        cmd_data.update({"cmd":"osascript","args":"-e 'tell application "+one+"Finder"+one+" to set desktop picture to POSIX file "+one+"/var/picture.jpg"+one+"'"})
        picture = session.send_command(cmd_data).strip()
        return ""
