#!/usr/bin/python2
#filename:continue.py

while True:
    s=raw_input('Enter something:')
    if s=='quit':
        break
    if len(s)<3:
        continue
    print 'input is of sufficient length'
    #do other kinds of work here...
