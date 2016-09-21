#!/usr/bin/python2
#filename:backup_ver1.py

import os
import time

#1 the files and dirs to be backedup are specified in a list
source=['/tmp/files/aa','/tmp/files/bb','/tmp/files/c']

#2 the backup must be stored in a main backup dir
target_dir='/tmp/backup/' #remember to change this to what you willing to use

#3 files are  backuped in a zip file
#4 name of the current zip file is data and time
today=target_dir+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')

#create dir if not exist
if not os.path.exists(today):
    os.mkdir(today) 
    print 'Successfully created dir',today

#take a comment from user to creat  the name of zip
comment=raw_input('Enter a comment-->')
if len(comment)==0:
    target=today+os.sep+now+'.zip'
else:
    target=today+os.sep+now+'_'+\
        comment.replace(' ','_')+'.zip'

#5 we use zip command to put  files in a zip file
zip_command="zip -qr '%s' %s"%(target,' '.join(source))

#run the  backup
if os.system(zip_command)==0:
    print 'Success backup to ',target
else:
    print 'Backup failed'
