# -*- coding: utf-8 -*-

people = 50
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is grooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

if 2 == 3 or False :
    print "People are hello."
else :
    print "some error"

if raw_input("input something: ") == "hello":
    print "input is hello"
else :
    print "input is not hello"
