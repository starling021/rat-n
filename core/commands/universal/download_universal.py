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

import json
import os
import core.helper as h
import re

class command:
	def __init__(self):
		self.name = "download"
		self.description = "Download remote file."
		self.usage = "Usage: download <remote_path>"
		self.type = "native"

	def run(self,session,cmd_data):
		if not cmd_data['args']:
            		print self.usage
            		return
		
		remote_path = os.path.split(cmd_data['args'])[-1]
		h.info_general("Downloading {0}...".format(remote_path)
		data = session.download_file(cmd_data['args'])
		if data:
			# save to downloads
			h.info_general("Saving {0}...".format(remote_path)
			f = open(os.path.join('downloads',remote_path),'w')
			f.write(data)
			f.close()
			h.info_success("Saved to downloads/"+remote_path+"!")
