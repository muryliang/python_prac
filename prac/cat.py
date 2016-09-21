#!/usr/bin/python2
#filename:cat.py

import sys

def readfile(filename):
    '''print a file to stand output'''
    f=file(filename)
    while True:
        line=f.readline()
        if len(line)==0:
            break
        print line, #notice comma
    f.close()
    

#Scripting starts from here
if len(sys.argv)<2:
    print 'No action specified'
    sys.exit()

if sys.argv[1].startswith('--'):
    option=sys.argv[1][2:]
    #fetch sys.argv[1] but without first two characters
    if option=='version':
        print 'Version 1.2'
    elif option=='help':
        print '''\
This program prints files to the standard output.
any number of files can be specified.
Options include:
    --version: prints the version number
    --help: Display this help'''
    else:
        print 'Unknown option.'
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)
