#!/usr/bin/python2

import functools

def execute(string):
    def log(func):
        @functools.wraps(func)
        def wrapper(*args, **kv):
            print '%s %s():'% (string,func.__name__)
            return func(*args, **kv)
        return wrapper
    return log

@execute('handling')
def now():
    print '2013-2-2'

now()
print 'now name is %s'% now.__name__
