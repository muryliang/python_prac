# -*- coding: utf-8 -*-

print "now start a game! Test your computer perfer!"

size = raw_input("You like big or small computer? #1 big #2 small\n> ")

if size == "1":
    print "you prefer performance or price? "
    print "#1 performance"
    print "#2 price"
    prefer = raw_input("> ")

    if prefer == "1":
        print "choose Xeon!!"
    elif prefer == "2" :
        print "choose shenzhou!!"
    else :
        print "well, you choose both, go die!!"

elif size == "2":
    print "you like small one , choose a note book!!"

else:
    print "you should avoid a computer in your life"


