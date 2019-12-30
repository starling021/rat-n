import modules.helper as h

class command:
    def __init__(self):
        self.name = "msh"
        self.description = "Mouse (MPL) Shell."
    
    def run(self,session,cmd_data):
        while 1:
	    #prepare command
	    msh = raw_input("msh# ")
            if msh == "exit":
                return
            else:
		if not msh['args']:
			argvs = ""
		else:
			argvs = msh['args']
		msh_command = {"cmd": msh, "args":argvs}
		result = session.send_command(msh_command)
		if result:
			print(result)
