#!/usr/bin/python2
#filename:finally.py

import time

try:
    f=file('poem.txt')
    while True:
        line=f.readline()
        if len(line)==0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()
    print 'Cleaning up...closed file'
