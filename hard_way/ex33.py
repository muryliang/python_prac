# -*- coding: utf-8 -*-


def loop(index, stride=1):
    i = 0
    numbers = []

    for i in range(0, index, stride):
        numbers.append(i)
#    while i < index:
#        print "At the top i is %d" %i
#        numbers.append(i)
#
#        i = i + stride
#        print "Numbers now: ", numbers
#        print "At the bottom i is %d" %i

#    print "The numbers: "

    for num in numbers:
        print num

index = int(raw_input("input your indice: "))
hop = int(raw_input("input hop: "))
loop(index, hop)

print "the int value of string 20 is %d" %int('20')
