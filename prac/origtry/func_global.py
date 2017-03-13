#!/usr/bin/python2
#filename:func_global.py

def func():
    global x
    
    print 'x is',x
    x=2
    print 'Change local x to',x

x=50
func()
print 'value of x is',x
