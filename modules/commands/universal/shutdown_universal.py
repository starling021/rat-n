class command:
	def __init__(self):
		self.name = "shutdown"
		self.description = "Shutdown device."

	def run(self,session,cmd_data):
		session.send_command({"cmd":"shutdown","args":""})
