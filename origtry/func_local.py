#!/usr/bin/python2
#filename:func_local.py

def func(x):
    print 'x is',x
    x=2
    print 'Changed local x to',x

x=50
print func(x)
print 'x is still',x
