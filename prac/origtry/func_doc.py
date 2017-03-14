#!/usr/bin/python2
#filename:func_doc.py

def printMax(a,b):
    '''prints the maxmum of the two numbers.

    then two values should be integers'''
    x=int(a)
    y=int(b)

    if x>y:
        print x,'is maximum'
    else:
        print y,'is maximum'

printMax(3,5)
print printMax.__doc__
