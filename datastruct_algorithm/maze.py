import turtle
import random
import pprint

class route():
    """draw the whole map"""

    def __init__(self, rate=0.5, color='brown', backcolor='white', pensize=3, blks=10, dest = (0,0)):
        self.dest = dest
        self.blks = blks
        self.pensize = pensize
        self.color = color
        self.backcolor = backcolor
        self.rate = rate
        self.map = list()

        self.turtle = turtle.Turtle()
        t = self.turtle
        self.screen = turtle.Screen()
        s = self.screen
        self.unith = s.window_height() // blks
        self.unitw = s.window_width() // blks
        t.pensize(pensize)

        # draw every blocks with rate
#        for i, j in ((x,y) for x in range(blks) for y in range(blks)):
        for i in range(blks):
            self.map.append(list())
            for j in range(blks):
                t.up()
                t.goto(i * self.unitw - 320, j * self.unith - 300)
                if random.random() > rate or (i, j) == (0, 0) or (i, j) == dest:
                    t.fillcolor(backcolor)
                    self.map[-1].append(['empty', 0]) # 0 means not visited yet
                else:
                    t.fillcolor(color)
                    self.map[-1].append(['block', 0])
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
        self.x = x 
        self.y = y
        t.up()
        t.goto(x * self.unitw - 320, y * self.unith - 300)
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

    def isDest(self):
        """if is destination, return ture"""

        if not self.available(self.x, self.y):
            return False
        if self.dest == (self.x, self.y):
            print ("found dest!!")
            return True

    def available(self, x, y):
        """whether current position can be forwarded"""

        if x < 0 or x >= self.blks or y < 0 or y >=self.blks:
            return False
        if self.map[x][y][0] == 'block' or self.map[x][y][1] == 1:
            return False
        return True

    def start(self):
        """finding and color the path

        from current start position, first go north,
        if wall or already visited , change to other directions;
        if all direction failed, go back one step
        if get to exit pot, return true, then recursively mark
        points on that path green
        """
        if self.search(self.x, self.y):
            print ("found a way")
        else:
            print ("not found")

    def search(self, x, y):
        """this function do recursive search"""

        assert self.map[x][y][0] != 'block' and self.map[x][y][1] != 1
        self.turtle.up()
        self.setPos(x, y)
        self.turtle.down()
        if self.isDest(): # if is destination, return true
            self.drawCircle(color='green')
            return True
        else:
            self.drawCircle(color='black')
        self.map[x][y][1] = 1 #mark visited

        res = False
        if not res and self.available(x, y+1):
            res = self.search(x, y+1)
        if not res and self.available(x, y-1):
            res = self.search(x, y-1)
        if not res and self.available(x-1, y):
            res = self.search(x-1, y)
        if not res and self.available(x+1, y):
            res = self.search(x+1, y)

        self.turtle.up()
        self.setPos(x, y)
        self.turtle.down()
        if res:
            self.drawCircle(color='green')
        else:
            self.drawCircle(color='red')
        return res
        
blks = 10
rate = 0.3
turtle.delay(1)
r = route(rate = rate, blks = blks, dest = (8,7))
pprint.pprint(r.map)
#turtle.delay(10)
r.setPos(0,0)
r.start()
r.screen.exitonclick()
