#!/usr/bin/env python3

import time
import json
import os
import core.helper as h

class command:
    def __init__(self):
        self.name = "icons"
        self.description = "List system alert icons."

    def run(self,session,cmd_data):
        os.system("sort data/icons/icons.txt")
