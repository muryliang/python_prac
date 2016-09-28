#!/usr/bin/python2
#filname:partial.py

import functools

int2 = functools.partial(int, base = 2)

print int2('100100')
print int2('20', base = 16)
