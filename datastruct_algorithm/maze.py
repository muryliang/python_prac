import turtle
import random

class route():
    """draw the whole map"""

    def __init__(self, rate=0.5, color='brown', backcolor='white', pensize=3, blks=10):
        self.blks = blks
        self.pensize = pensize
        self.color = color
        self.backcolor = backcolor
        self.rate = rate

        self.turtle = turtle.Turtle()
        t = self.turtle
        self.screen = turtle.Screen()
        s = self.screen
        self.unith = s.window_height() // blks
        self.unitw = s.window_width() // blks
        t.pensize(pensize)

        # draw every blocks with rate
        for i, j in ((x,y) for x in range(blks) for y in range(blks)):
            t.up()
            t.goto(j * self.unitw - 320, i * self.unith - 300)
            if random.random() <= rate:
                t.fillcolor(color)
            else:
                t.fillcolor(backcolor)
            t.down()
            t.begin_fill()
            t.seth(90)
            t.forward(self.unitw)
            t.right(90)
            t.forward(self.unith)
            t.right(90)
            t.forward(self.unitw)
            t.right(90)
            t.forward(self.unith)
            t.end_fill()

    def setPos(self, x, y):
        """set cursor's position"""

        t = self.turtle
        self.x = x * self.unitw - 320;
        self.y = y * self.unith - 300;
        t.up()
        t.goto(self.x, self.y)
        t.down()

    def drawCircle(self, color='black'):
        """draw circle at current position"""

        t = self.turtle
        t.seth(0)
        t.up()
        t.forward(self.unitw / 2)
        t.left(90)
        t.forward(self.unith / 4)
        t.right(90)
        t.fillcolor(color)
        t.down()
        t.begin_fill()
        t.circle(min(self.unitw/4, self.unith/4))
        t.end_fill()

    def start(self):
        """finding and color the path

        from current start position, first go north,
        if wall or already visited , change to other directions;
        if all direction failed, go back one step
        if get to exit pot, return true, then recursively mark
        points on that path green
        """

        x = self.x
        y = self.y
        
blks = 5
rate = 0.2
turtle.delay(1)
r = route(rate = rate, blks = blks)
r.setPos(0,0)
r.drawCircle()
r.screen.exitonclick()
