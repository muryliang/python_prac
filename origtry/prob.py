#!/usr/bin/python2
#filename:prob.py

a = [1,2,3,4,5]

def prob(a):
    return reduce(lambda x,y: x*y, a)

print prob(a)
