import modules.helper as h

class command:
    def __init__(self):
        self.name = "msh"
        self.description = "Mouse (MPL) Shell."
	
    def msh(self):
	os.system("printf '\033]2;Mouse CLI\a'")
        return h.GREEN+ "[" + self.hostname + h.WHITE + "@" + h.GREEN + self.username + h.ENDC + " " + WHITE_C + self.current_directory + h.GREEN + "]" + h.WHITE + "$ " + h.ENDC
    
    def run(self,session,cmd_data):
        while 1:
	    #prepare command
	    msh = raw_input(self.msh())
		
	    if not raw or raw.replace(" ","") == "":
	        continue
	    mshd = raw.split()[0]
	    mshd_data = {"cmd": cmd, "args":msh[len(mshd) + 1:]}
	    if mshd == "exit":
                return
            else:
		try:
		    result = session.send_command(mshd_data)
		    if result:
			print result.rstrip()
		except KeyboardInterrupt:
	            session.send_command({"cmd":"killtask"})
