class command:
    def __init__(self):
        self.name = "getpass"
        self.description = "Retreive the device passcode."
    
    def run(self,session,cmd_data):
        error = session.send_command(cmd_data)
        if error:
        	print(h.RED+"[-]"+h.WHITE+" Can't retreive device passcode!")
