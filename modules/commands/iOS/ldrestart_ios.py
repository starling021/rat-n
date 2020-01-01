class command:
	def __init__(self):
		self.name = "reboot"
		self.description = "Restart iOS kernel."

	def run(self,session,cmd_data):
		session.send_command({"cmd":"ldrestart","args":""})
