import fileinput as fi                   #  1
                                         #  2
for line in fi.input(inplace=True):      #  3
    line = line.rstrip()                 #  4
    num = fi.lineno()                    #  5
    print "%-40s # %2i"%(line, num)      #  6
                                         #  7
