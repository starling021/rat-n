import modules.helper as h

class command:
    def __init__(self):
        self.name = "bundleids"
        self.description = "List bundle identifiers."
    
    def run(self,session,cmd_data):
        print h.WHITEBU+"Bundle Identifiers:"+h.ENDC
        print session.send_command(cmd_data).rstrip()
