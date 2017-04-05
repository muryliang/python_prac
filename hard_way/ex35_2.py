# -*- coding: utf-8 -*-

from sys import exit 

def one_room():
    print "you are now in room one, choose left or right."
    while True :
        choice = raw_input("> ")

        if choice == "left" :
            two_room()
        elif choice == "right":
            three_room()
        else:
            print "reselect"

def two_room() :
    print "you are now in room two, choose 1 or 2."
    while True:
        choice = int(raw_input("> "))
        if choice == 1:
            over("you choose first")
        elif choice == 2:
            over("you choose second")
        else:
            print "choose again"

def three_room() :
    print "you are now in room three, choose 3 or 4."
    while True:
        choice = int(raw_input("> "))
        if choice == 3:
            over("you choose three")
        elif choice == 4:
            over("you choose four")
        else:
            print "choose again"

def over(s):
    print s,"Bye!"
    exit(0)

def start():
    one_room()

start()
