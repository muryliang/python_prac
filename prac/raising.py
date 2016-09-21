#!/usr/bin/python2
#filename:raising.py

class ShortInputException(Exception):
    '''A user-defined exception class'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast

try:
    s=raw_input('Enter something-->')
    if len(s)<3:
        raise ShortInputException(len(s),3)
except EOFError:
    print '\nwhy did you do an eof to me?, %d'%x.length
except ShortInputException:
    print 'I am in short input'
#    print 'ShortInputException: the input was of length %d,\
#        was excepting at least %d'%(x.length,x.atleast)
else:
    print 'No exception was raised'
