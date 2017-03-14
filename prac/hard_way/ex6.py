# -*- coding: utf-8 -*-

#this s a format string with number as param
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#this another format string with tuple as param
y = "Those who know %r and those who %s." %(binary, do_not)

#just print those strings, with format
print x
print y

#%r output will output string with ' '
print "I said: %r." %x
#%s output will just output, also formatted
print "I said y: %s." %y
print "I also said: '%s'." %y

hilarious = True #False
joke_evaluation = "Isn't that joke so funny?! %s" # == %r, and %d will output 1 

#this format of print also works
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#add string togegher, with no blank between them
print w + e 
