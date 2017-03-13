#!/usr/bin/python2
#filename:calibrate

list = ['adam','LISA','barT']

def calibrate(a):
    return map(lambda string: string[0].upper() + string.lower()[1:], a)

print list
print calibrate(list)
