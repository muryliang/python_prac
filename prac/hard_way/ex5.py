# -*- coding: utf-8 -*-

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inch_to_cent = 2.45
pound_to_kilo = 1 / 2.2046

print "Let's talk about %s." % name
print "He's %d inches tall." % height,
print "and height in cent is %.2f" % (height * inch_to_cent)
print "He's %d pounds heavy." %weight,
print "and pound to kilo is %.2f" %(weight * pound_to_kilo)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

#this line is trick, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(
    age, height, weight, age + height + weight)
print 'try print %s'%(2+3)
