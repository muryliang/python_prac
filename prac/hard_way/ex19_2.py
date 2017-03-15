# -*- coding: utf-8 -*-

def myfunc(one=100, two=200):
    print "one is",one
    print "two is",two

print "start by pass const"
myfunc(1, 2)

first = 20
second = 30
print "pass vars"
myfunc(first, second)

print "pass cal of val"
myfunc(first + 20, second + 30)

print "pass by assign"
myfunc()
