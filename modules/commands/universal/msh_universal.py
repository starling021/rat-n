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
		result = session.send_command(cmd_data)
		if result:
		    print result.rstrip()
