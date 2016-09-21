#!/usr/bin/python2
#filename:if.py

number=23
guess=int(raw_input('enter an integer:'))

if guess==number:
    print'Congratulations you guessed it!'#block start here
    print"(but you do not win any prize!)"#block end here
elif guess<number:
    print 'no,it is a little higher than that' #another block
    #you can do whatever you like here
else:
    print 'no,it is a little lower than that'
    #you must have guess > number to reach here
print 'Done'
#This last statement is always executed, after the if statement is executed!
