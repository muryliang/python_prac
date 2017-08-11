import time
import sys
import turtle

def move(num, start, end, mid):
    """move from start to end, use mid to tmp store"""

    global count
    if num == 0:
        return
    move(num-1, start, mid, end)
    do_move(start, end, num)
    count += 1
    move(num-1, mid, end, start)

def do_move(start, end, num):
    global s
    print ("move panel %d from %d to %d"%(num, start, end))
    s[end-1].append(s[start-1].pop())
    redraw(s)

def redraw(s):
    global t
    height = -200
    t.clear()
    start = -200
    t.up()
    t.goto(start, height)
    for i in range(3):
        turtle.tracer(100)
        for length in s[i]:
            drawTangle(length)
        t.up()
        t.goto(start + (i+1)*200, height)
        turtle.tracer(1)
        time.sleep(0.5)

def drawTangle(length):
    global t
    length *= 1
    width=10
    t.down()
    t.seth(180)
    t.fd(length/2)
    t.seth(90)
    t.fd(width)
    t.seth(0)
    t.fd(length)
    t.seth(270)
    t.fd(width)
    t.seth(180)
    t.fd(length/2)
    t.up()
    t.seth(90)
    t.fd(width)

s = list()
for _ in range(3):
    s.append(list())

turtle.delay(5)
t = turtle.Turtle()
scr = turtle.Screen()

numbers = int(sys.argv[1])
for i in range(numbers, 0, -1):
    s[0].append(i)

count = 0
tick = time.time()
move(numbers, 1, 3, 2)
print ("all cost %d steps, time %f"%(count, time.time() - tick))
scr.exitonclick()

