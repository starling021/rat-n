class command:
    def __init__(self):
        self.name = "brightness"
        self.description = "Adjust screen brightness."
        self.usage = "Usage: brightness <level: 0.0>"
        self.type = "native"
    
    def run(self,session,cmd_data):
        try:
            float(cmd_data["args"])
        except:
            print self.usage
            return
        session.send_command(cmd_data)
