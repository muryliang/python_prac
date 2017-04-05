#!/usr/bin/python2
#filename:reference.py

print 'Simple Assignment'
shoplist=['apple','mango','carrot','banana']
mylist=shoplist

del shoplist[0]

print 'shoplist is',shoplist
print 'mylist is',mylist
#notice shoplist and mylist both print  the same list without
#apple confirming that they point to the same object

print 'Copy by making a full slice'
mylist=shoplist[:]
del mylist[0]

print 'shoplist is',shoplist
print 'mylist is',mylist

