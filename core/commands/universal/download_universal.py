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
		self.usage = "Usage: download <remote_path> <local_path>"
		self.type = "native"

	def run(self,session,cmd_data):
		if not cmd_data['args']:
            		print self.usage
            		return
        	else:
            		paths = re.split(r'(?<!\\) ', cmd_data['args'].rstrip())
            	if len(paths) > 2:
                	print "Usage: download <remote_path> <local_path>"
                	return
            
            	local_dir = os.path.split(paths[0])[0]
            	local_file = os.path.split(paths[0])[1]
            
            	if len(paths) == 1:
                	remote_dir = "."
                	remote_file = local_file
            	else:
                	remote_dir = os.path.split(paths[1])[0]
                	if not remote_dir:
                    		remote_dir = "."
                	remote_file = os.path.split(paths[1])[1]
                	if not remote_file:
                    		remote_file = local_file
		
		h.info_general("Downloading {0}...".format(file_name))
		data = session.download_file(cmd_data['args'])
		if data:
			# save to downloads
			h.info_general("Saving {0}...".format(file_name))
			f = open(os.path.join(paths[0],remote_dir),'w')
			f.write(data)
			f.close()
			h.info_success("Saved to downloads/{0}!".format(file_name))
