#!/usr/bin/python

class mclass:
    def __init__(self,c=10,d=20):
        a=c
        b=d
        print 'done'

    def __del__(self):
        print 'about to del'

print 'use a class'
cl=mclass(13)
print 'haha, going close'
