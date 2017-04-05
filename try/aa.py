from sys import exit
a = 10
b = 0
try:
    c = a /b
    print c
except ZeroDivisionError, e:
    print e.message
    exit(1)
finally:
    print 'haha'
print "done"
