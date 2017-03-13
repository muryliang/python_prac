#!/usr/bin/python2

a = {'a':4, 'b':'apple', 'c':20.5}
print a
print 'now append'
a['d'] = 'hello'
print a
print 'now delete'
del a['a']
print 'modify'
a['b'] = 'pear'
print a
print 'now iterate'
for e,f in a.items():
    print e,' and ',f,' ',

