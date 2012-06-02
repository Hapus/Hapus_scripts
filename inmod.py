#!/usr/bin/env python

import os
import sys

#Module list
module_list = sys.argv[1:]

#Clear out screens
os.system("clear")
print "Installing modules (" + str(len(module_list)) + ")"

#Drupal paths
local_path = " -r /Users/avadhutp/Sites/hapus "

#Install all modules
for module in module_list:
	print "Installing " + module
	os.system("drush dl " + local_path + module)
	os.system("drush en -y" + local_path + module)
	os.system("drush cc all")