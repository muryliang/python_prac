#!/usr/bin/python2

class person(object):
    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        if path == 'user' :
            def wrapper(*args , **kw):
                arg = args[0]
                if arg == '':
                    arg = 'default'
                return person('%s/%s'%(self._path, arg ))
            return wrapper
        else:
            return person('%s/%s'%(self._path, path))

    def __str__(self):
        return self._path

print person().user('').user('').haha.hehe.hihi
        
