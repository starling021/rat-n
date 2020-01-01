class command:
	def __init__(self):
		self.name = "ldrestart"
		self.description = "Restart the kernel."

	def run(self,session,cmd_data):
		session.send_command({"cmd":"ldrestart","args":""})
