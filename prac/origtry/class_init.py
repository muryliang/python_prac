#!/usr/bin/python2
#filename:class_init.py

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sayhi(self):
        print 'hello,my name is %s and age is %d'%(self.name,self.age)

p=Person('mury',int('12'))
p.sayhi()
