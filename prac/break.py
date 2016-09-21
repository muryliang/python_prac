#!/usr/bin/python2
#filename:break.py

while True:
    s=raw_input('Enter something:')
    if s=='quit':
        break
    print 'Length of th string is',len(s)
print 'Done'
