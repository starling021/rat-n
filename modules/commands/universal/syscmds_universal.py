import modules.helper as h

class command:
    def __init__(self):
        self.name = "syscmds"
        self.description = "Display all system commands."
    
    def run(self,session,cmd_data):
        payload = "-c | sort"
        cmd_data.update({"cmd":"compgen","args":payload})
        print("\nSystem Commands")
        print("===============")
        print("")
        print session.send_command(cmd_data)
