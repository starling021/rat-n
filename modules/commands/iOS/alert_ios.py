import base64
import json

class command:
    def __init__(self):
        self.name = "alert"
        self.description = "Make alert show up on device."
        self.type = "native"

    def run(self,session,cmd_data):
        title = raw_input("Title: ")
        message = raw_input("Message: ")
        session.send_command({"cmd":"alert","args":json.dumps({"title":title,"message":message})})
        return ""
