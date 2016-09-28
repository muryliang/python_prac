#!/usr/bin/python2
#filename:decorate2.py

import functools

def log(text):
    if callable(text):
        @functools.wraps(text)
        def wrapper(*argv, **kv):
            print 'begin,call',
            text(*argv, **kv)
            print 'end call'
        return wrapper
    else:
        def decorate(func):
            @functools.wraps(func)
            def wrapper(*argv, **kv):
                print 'begin,call',text
                func(*argv, **kv)
                print 'end call'
            return wrapper
        return decorate


@log
def now():
    print 'it is now in'

now()

@log('execute')
def now():
    print 'that is now in'

now()
