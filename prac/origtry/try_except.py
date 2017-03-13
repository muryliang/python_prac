#!/usr/bin/python2
#filename:try_except.py

import sys

try:
    s=raw_input('Enter something-->')
except EOFError:
    print '\nwhy did you do an EOF error for me?'
    sys.exit()
except:
    print '\nsome error/exception occurred'
    #here we are not exiting program

print 'Done'
