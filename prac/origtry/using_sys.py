#!/usr/bin/python2
#filename:using_sys.py

import sys
print 'the command line arguments are:'
for i in sys.argv:
    print i

print '\n\nTHE PYTHONPATH is',sys.path,'\n'
print sys.argv
