import turtle

def draw(t, level, direction, length):
    if level == 1:
        drawUnit(t, direction, length)
    else: 
        if direction == 'left':
            draw(t, level-1, 'up', length)
            t.seth(0) # east
            t.forward(length)
            draw(t, level-1, 'left', length)
            t.seth(270)
            t.forward(length)
            draw(t, level-1, 'left', length)
            t.seth(180)
            t.forward(length)
            draw(t, level-1, 'down', length)
        elif direction == 'right':
            draw(t, level-1, 'down', length)
            t.seth(180) # east
            t.forward(length)
            draw(t, level-1, 'right', length)
            t.seth(90)
            t.forward(length)
            draw(t, level-1, 'right', length)
            t.seth(0)
            t.forward(length)
            draw(t, level-1, 'up', length)
        if direction == 'up':
            draw(t, level-1, 'left', length)
            t.seth(270) # east
            t.forward(length)
            draw(t, level-1, 'up', length)
            t.seth(0)
            t.forward(length)
            draw(t, level-1, 'up', length)
            t.seth(90)
            t.forward(length)
            draw(t, level-1, 'right', length)
        if direction == 'down':
            draw(t, level-1, 'right', length)
            t.seth(90) # east
            t.forward(length)
            draw(t, level-1, 'down', length)
            t.seth(180)
            t.forward(length)
            draw(t, level-1, 'down', length)
            t.seth(270)
            t.forward(length)
            draw(t, level-1, 'left', length)

def drawUnit(t, direction, length):
    if direction == 'up':
        t.seth(270)
        t.forward(length)
        t.seth(0)
        t.forward(length)
        t.seth(90)
        t.forward(length)
    elif direction == 'down':
        t.seth(90)
        t.forward(length)
        t.seth(180)
        t.forward(length)
        t.seth(270)
        t.forward(length)
    elif direction == 'left':
        t.seth(0)
        t.forward(length)
        t.seth(270)
        t.forward(length)
        t.seth(180)
        t.forward(length)
    elif direction == 'right':
        t.seth(180)
        t.forward(length)
        t.seth(90)
        t.forward(length)
        t.seth(0)
        t.forward(length)


t = turtle.Turtle()
s = turtle.Screen()
t.up()
t.goto(-320,300)
t.down()
turtle.delay(1)
dim = int(input("dimention: "))
turtle.tracer(1000)
draw(t, dim, 'up', 1)
turtle.tracer(0)
s.exitonclick()

