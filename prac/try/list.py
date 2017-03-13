#!/usr/bin/python2

print 'hahaha',
print 'hehe'

la = [1,2,3]
print la[1:]
print la
del la[1]
la.append(3)
print 'the length of la is ',len(la)
bb = la[2]
la[2] = 5
print la
print 'bb is ',la[2]
print 'length is ',len(la)
try: 
    1 > 2
except: raise EOFError
finally: 
    print 'haha'

print 'try two string','haha'
print 'I want to use *regular*'
