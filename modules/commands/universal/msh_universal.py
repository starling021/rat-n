import modules.helper as h
import json
import os

class command:
    def __init__(self):
        self.name = "msh"
        self.description = "Open target device shell."
	self.username = device_info['username'].encode("utf-8")
	self.hostname = device_info['hostname'].encode("utf-8")
	self.type = device_info['type']
	self.uid = device_info['uid']
	self.current_directory = device_info['current_directory'].encode("utf-8")
	if self.uid == "0":
		whoami = "# "
	else:
		whoami = "$ "
	
    def msh(self):
	os.system("printf '\033]2;Mouse Shell\a'")
        return h.RED+self.username+"@"+self.hostname+h.WHITE+":"+self.current_directory+whoami
    
    def run(self,session,cmd_data):
        while 1:
	    #prepare command
	    msh = raw_input(self.msh())
	    if not msh or msh.replace(" ","") == "":
	        continue
	    mshd = msh.split()[0]
	    mshd_data = {"cmd": mshd, "args":msh[len(mshd) + 1:]}
	    if mshd == "cd":
		result = json.loads(session.send_command(mshd_data))
                if 'error' in result:
        	    h.info_error(result['error'])
                elif 'current_directory' in result:
        	    session.current_directory = result['current_directory'].encode('utf-8')
                else:
        	     h.info_error('Unable to get current directory!')
	    if mshd == "ls":
                if not mshd_data['args']:
                    mshd_data['args'] = '.'
                data = session.send_command(mshd_data)
                try:
                    contents = json.loads(data)
                except:
                    print data
                    return
                keys = contents.keys()
                keys.sort()
                for k in keys:
                    if contents[k] == 4 or contents[k] == 10:
                        print h.COLOR_INFO + k + h.ENDC
                    else:
                        print k
	    if mshd == "exit":
                return
	    else:
		try:
		    result = session.send_command(mshd_data)
		    if result:
		        if mshd == "ls" or mshd == "cd":
			    pass
			else:
			    print result.rstrip()
		except KeyboardInterrupt:
	            session.send_command({"cmd":"killtask"})
