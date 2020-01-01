class command:
	def __init__(self):
		self.name = "reboot"
		self.description = "Shutdown device."

	def run(self,session,cmd_data):
		session.send_command({"cmd":"shutdown","args":"-r now"})
