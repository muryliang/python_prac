import sys
try:
    s = raw_input("input something--> ")
    print s
except EOFError:
    print "eof error"
#    sys.exit(0)
except :
    print "error happen"
print 'done'
