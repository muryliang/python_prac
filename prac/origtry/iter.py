#!/usr/bin/python2
#filename:iter.py

class person(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self # this used by next to do iteration

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 20:
            raise StopIteration()
        return self.a


b = person()

for i in b:
    print i
