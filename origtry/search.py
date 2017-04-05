#!/usr/bin/python2
#filename:search.py

import os

def search(path):
    try:
        for name in os.listdir(path) :
            fullname = os.path.join(path,name)
            if not os.path.isdir(fullname):
                print 'file',fullname
            else: #subdir
                search(fullname)
    except StandardError,e:
        print '%s;haha path: %s'%(e,path)
    

mypath = raw_input('enter a path=>')

if os.path.exists(mypath):
    search(mypath)
else:
    print 'no such path:',mypath
