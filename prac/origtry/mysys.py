#!/usr/bin/python2
#-*- coding: utf-8 -*-
#filename:sys.py

'just for fun'


import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print 'hello, world'
    elif len(args) == 2:
        print 'hello, %s'%args[1]
    else:
        print 'too many args'

if __name__ == '__main__':
    test()
else:
    print 'in others'
