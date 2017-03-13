#!/usr/bin/python2

#with open("/etc/passwd", 'r') as f:
try:
    f = open("/etc/paswd", 'r')
    for line in f.readlines():
        print line.strip()
except IOError,e:
    print 'error',e
finally:
    f.close()
