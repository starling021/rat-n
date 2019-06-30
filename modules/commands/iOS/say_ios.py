class command:
    def __init__(self):
        self.name = "say"
        self.description = "Text to speach."
        self.usage = "Usage: say <text>"
    
    def run(self,session,cmd_data):
    	if not cmd_data['args']:
    		print self.usage
        session.send_command(cmd_data)
