class command:
    def __init__(self):
        self.name = "syscmds"
        self.description = "Display all system commands."
    
    def run(self,session,cmd_data):
        payload = "-c"
        cmd_data.update({"cmd":"compgen","args":payload})
        print session.send_command(cmd_data)
