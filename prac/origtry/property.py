#!/usr/bin/python2
#filename:property.py

class person(object):
    def __init__(self, name,var):
        self.name = name
        self.num = var

    @property
    def value(self):
        return self.num

    @value.setter
    def value(self, var):
        self.num = var


b = person('mury', 12)
print b.value
b.value = 20
print b.value
