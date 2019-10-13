class command:
    def __init__(self):
        self.name = "say"
        self.description = "Convert text to speach."
        self.usage = "Usage: say <text>"
    
    def run(self,session,cmd_data):
    	if not cmd_data['args']:
    		print self.usage
        payload = cmd_data['args']
        cmd_data.update({"cmd":"say","args":payload})
