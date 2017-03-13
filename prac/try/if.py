#!/usr/bin/python

b=raw_input("input your integer:")
'''
if a=='2':
    print ' you are 2'
elif a=="3":
    print 'you are 3'
else:
    print 'your are nothing'

a = int(b)
while a > -20:
    print 'now is ', a
    a = a-1
else :
    print 'now done'

'''

a = int(b)
for x in range(0,a+1):
    if x % 3 == 0:
        continue
    print x,
    if x == 10:
        break
else:
    print '\nover'
