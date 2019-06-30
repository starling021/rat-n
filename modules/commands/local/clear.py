import os

class command:
    def __init__(self):
        self.name = "clear"
        self.description = "Clean terminal input/output."
    
    def run(self,session,cmd_data):
        os.system('clear')

