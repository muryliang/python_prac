import sys
try:
    s = raw_input("input something--> ")
    print s
except :
    print "error happen"
except EOFError:
    print "eof error"
#    sys.exit(0)
print 'done'
