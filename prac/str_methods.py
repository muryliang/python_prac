#!/usr/bin/python2
#filename:str_methods.py

name='Swaroop'

if name.startswith('Swa'):
    print 'Yes, the string starts with "Swa"'

if 'a' in name:
    print 'Yes, it contains  the string  "a"'

if name.find('war')!=-1:
    print 'Yes, it contains the string "war"'

delimter='_*_'
mylist=['Brazil','Russia','India','China']
print delimter.join(mylist)
