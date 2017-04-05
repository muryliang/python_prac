#!/usr/bin/python

def hello(a=3,b=2):
    '''hello just a test

    this is a test func
    haha'''
    print 'first param is ',a
    print 'second param is %s'%b
    print 'now return'
    return 'hehe'

print 'after define now call'
hello(10,20)
print 'after define now call'
hello(1)
hello()
a=hello(b=20)
print 'return val is',a
#print 'doc is',hello.__doc__
help(hello)
