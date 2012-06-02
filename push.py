#!/usr/bin/env python

import os
import sys

#Clear the display for a clean output
os.system('clear')

#Get the argument list
options = sys.argv[1:]

#Beginning Modules push to live from Avadhut DEV
if 'modules' in options or 'all' in options:
	print 'Beginning Modules & Libraries folders push to live from Avadhut DEV...'
	os.system('drush -v rsync @dev:%modules @live:%modules')
	os.system('drush -v rsync @dev:%libraries @live:%libraries')

#Beginning SQL push to live from Avadhut DEV
if 'db' in options or 'all' in options:
	print 'Beginning database push to live from Avadhut dev...'
	os.system('drush -v sql-sync @dev @live')

#Beginning Themes push to live from Avadhut DEV
if 'themes' in options or 'all' in options:
	print 'Beginning Themes folder push to live from Avadhut dev...'
	os.system('drush -v rsync @dev:%themes @live:%themes')

#Clear remote cache
os.system('drush -v @live cc all')