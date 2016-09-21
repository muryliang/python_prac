#!/usr/bin/python2
#filename:pickling.py

import cPickle as p

shoplistfile='shoplist.data'

shoplist=['apple','mango','carrot']

f=file(shoplistfile,'w')
p.dump(shoplist,f)
f.close

del shoplist

f=file(shoplistfile)
storelist=p.load(f)
print storelist
