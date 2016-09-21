#!/usr/bin/python2
#filename:using_name.py

import using_name
print '2name is',__name__
if __name__=='__main__':
    print 'the program is running by itself'
else:
    print 'the program is running by other'
