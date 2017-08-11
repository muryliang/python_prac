import turtle
import math

def draw(t, start, end, limit):
    t.up()
    t.goto(start)
    length = t.distance(end)
    angle = t.towards(end)
    #left end/3 + start*2/3
    left = (1/3*end[0] + 2/3*start[0], 1/3*end[1] + 2/3*start[1])
    right = (1/3*start[0] + 2/3*end[0], 1/3*start[1] + 2/3*end[1])
    t.goto(0.5*(start[0] + end[0]), 0.5*(start[1] + end[1]))
    t.seth(angle)
    t.left(90)
    t.forward(length / 6 * math.sqrt(3))
    mid = t.pos()
    if length / 3 >= limit:
        draw(t, start, left, limit)
        draw(t, left, mid, limit)
        draw(t, mid, right, limit)
        draw(t, right, end, limit)
    else:
        t.up()
        t.goto(start)
        t.down()
        t.goto(left)
        t.goto(mid)
        t.goto(right)
        t.goto(end)

t = turtle.Turtle()
s = turtle.Screen()
height = -100
length = 10
turtle.tracer(100)
turtle.delay(1)
t.up()
t.goto(-200, height)
t.seth(0)
t.left(60)
t.forward(400)
pos = t.pos()
draw(t, (200, height), (-200, height), length)
draw(t, (-200, height), pos, length)
draw(t, pos, (200, height), length)
turtle.tracer(1)
s.exitonclick()
