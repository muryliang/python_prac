#-*- coding: utf-8 -*-

from sys import argv #import so we can use argv

script, filename = argv #unpack argv to two args

txt = open(filename) #open a file, should in pwd

print "Here's your file %r:" %filename
print txt.read()  #read that file, will read all
txt.close()

print "Type the filename again:"
file_again=raw_input("> ") #prompt to read a filename 

txt_again = open(file_again) #open again using the same name as above
print txt_again.read() #read from this stdin input filename
txt_again.close()

