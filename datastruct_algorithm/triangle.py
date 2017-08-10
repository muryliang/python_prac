import turtle

def maketri(length, t):
    if length < 25:
        return
    t.begin_fill()
    t.right(60)
    t.forward(length)
    t.right(120)
    t.forward(length)
    t.right(120)
    t.forward(length)
    t.right(60) # make it point to origin direction
    t.end_fill()

    #upper one
    t.forward(length/2)
    maketri(length/2, t)
    t.backward(length/2)

    #lower one
    t.backward(length/2)
    maketri(length/2, t)
    t.forward(length/2)

    curpos = t.pos()
    t.right(60)
    t.forward(length)
    t.left(60)
    t.backward(length/2)
    maketri(length/2, t)
    t.up()
    t.setpos(curpos)
    t.down()

t = turtle.Turtle()
t.pensize(1)
t.color('black', 'pink')
t.begin_fill()
s = turtle.Screen()
turtle.delay(1)
t.up()
t.setposition(-200, -200)
t.setheading(90)
t.right(30)
t.down()
t.forward(400)
t.right(120)
t.forward(400)
t.right(120)
t.forward(400)
t.end_fill()
t.right(120)
t.forward(200)
t.color('red', 'blue')
maketri(200, t)
s.exitonclick()

    
