import time
import json
import os
import core.helper as h

class command:
    def __init__(self):
        self.name = "icons"
        self.description = "List system alert icons."

    def run(self,session,cmd_data):
        print("\nAlert Icons")
        print("===========")
        print("")
        os.system("sort data/icons/icons.txt")
        print("")
