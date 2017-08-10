import turtle
import math

def draw(p1, p2, t, length):
    if length < 10:
        return
    t.up()
    t.goto(p1)
    angle = t.towards(p2)
    t.down()
    t.goto(p2)
    t.up()
    pmid = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
    t.goto(pmid)
    t.seth(angle)
    t.left(90)
    t.forward(length / 2 / math.sqrt(3))
    pos = t.pos()
    t.down()
    t.goto(p1)
    t.goto(pos)
    t.goto(p2)
    draw(p1, pos, t, length/ math.sqrt(3))
    draw(pos, p2, t, length/ math.sqrt(3))
    
def smaller(p1, p2):
    if p1[1] < p2[1]:
        return True
    if p1[0] < p2[0]:
        return True
    return False


t = turtle.Turtle()
s = turtle.Screen()
turtle.delay(1)
draw((-200, -200), (200, -200), t, 400)
s.exitonclick()


