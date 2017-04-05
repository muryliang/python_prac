# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") #get an input actually, and CTRL-C will stop here

print "Opening the file..."
target = open(filename, 'w')  #open for write , will truncate auto

#print "Truncating the file. Goodbye!"
#target.truncate()           #I think this truncate not necessary

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ") #get one line
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#target.write(line1) #write that line ,the \n is stripped
#target.write('\n')
#target.write(line2)
#target.write('\n')
#target.write(line3)
#target.write('\n')

target.write("%s\n%s\n%s\n"%(line1, line2, line3))

print "And finally, we close it."
target.close()
