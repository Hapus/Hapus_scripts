#!/usr/bin/env python

import os
import time

#Settings
rhost = "sprintpdf.com"
rusername = "backupdb"
rpassword = "coldcold"

lusername = "root"
lpassword = "coldcold"


#Store the backup in the tmp folder
print "Beginning remote backup..."
filename = "/tmp/hapus_" + time.strftime("%Y_%m_%d_%H_%M", time.localtime()) + ".sql"
rcommand = "/usr/local/mysql/bin/mysqldump -u " + rusername + " -p" + rpassword + " -h" + rhost + " hapus> " + filename
os.system(rcommand)
print "Remote backup done. Starting local restore..."

#Start the local restore
lcommand = "/usr/local/mysql/bin/mysql -u " + lusername + " -p" + lpassword + " -Dhapus < " + filename
print lcommand
os.system(lcommand)
print "Local restore done."

#Delete the temp file
os.system("rm " + filename)
print "Temporary dump file deleted."