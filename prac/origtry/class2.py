#!/usr/bin/python2

class people(object):
    def __init__(self, name, age):
        self._name = name
        self._age  = age


class student(people):
    def get(self):
        print 'attr are %s %s'%(self._name, self._age)

b = student('mury', 12)
b.get()
