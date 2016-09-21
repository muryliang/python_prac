#!/usr/bin/python2
#filename:while.py

number=23
running=True

while running:
    guess=int(raw_input('Enter an integer:'))
    
    if guess==number:
        print 'Congratulations'
        running=False #This cause the loop break
    elif guess<number:
        print 'no, a little higher than that'
    else:
        print 'no, a little lower than that'
    
else:
    print 'the loop is done'

print 'Done'
