#!/usr/bin/python2


try:
    print 'trying...'
    r = 10 / 2
    print 'result  r is:',r
except ZeroDivisionError, e:
    print 'except:',e
else:
    print 'no error'
finally:
    print 'finally..'
print 'End'
