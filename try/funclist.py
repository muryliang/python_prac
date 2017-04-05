#!/usr/bin/python

def hello(aa,*bb,**cc) : #why show like this ??
    aa.append(len(aa))
    print 'aa is',aa
    print 'bb is',bb
    cc[23] = 23
    print 'cc is',cc

aa = [1,2,3,4,5]
bb = ('a', 'b', 'c')
cc = {21:11,22:12,23:13}
hello(aa,bb,cc)
dd = [3*i for i in aa if i > 3 and i < 5]
print 'dd is', dd
