class command:
    def __init__(self):
        self.name = "idletime"
        self.description = "Get the amount of time since the keyboard/cursor were touched."
        self.type = "native"

    def run(self,session,cmd_data):
        print session.send_command(cmd_data)
