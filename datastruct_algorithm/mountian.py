import turtle
import math

def draw(p1, p2, t, length):
    t.up()
    t.goto(p1)
    angle = t.toward(p2)
    t.down()
    t.goto(p2)
    t.up()
    pmid = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
    t.goto(pmid)
    t.seth(angle)
    if smaller(p2, p1):
        t.left(90)
    else:
        t.right(90)
    t.down()
    t.forward(length / 2 / math.sqrt(3))
    pos = t.pos()
    t.goto(p1)
    t.goto(pos)
    t.goto(p2)
    draw(p1, pos, length/ math.sqrt(3))
    draw(pos, p2, length/ math.sqrt(3))
    
def smaller(p1, p2):
    if p1[1] < p2[1]:
        return True
    if p1[0] < p2[0]:
        return True
    return False


t = turtle.Turtle()
s = turtle.Screen()

draw((-200, -200), (200, -200), t)


