#!/usr/bin/python2
#filename:filter.py

from math import sqrt

n = int(raw_input('input a range=>'))


#print isprime()

def isprime(a):
    return 0 not in [a % b for b in range(2, int(sqrt(a))+1)]

a =  filter(isprime, range(2,n))
print 'list is',a,'length is',len(a)
