import pprint
import random
class cheese(object):
    def __init__(self, size):
        """
        initialize chess table, record size
        initialize to 0
        """
        self.size = size;
        self.inc = 0
        self.tbl = [[0] *size for i in range(size)]

    def get(self, x, y):
        """
        get the chess position info in one position
        1 or 0
        """
        return self.tbl[x][y]

    def set(self, x, y):
        """
        set that position to 1
        """
        self.tbl[x][y] = 1

    def unset(self, x, y):
        """
        set that position to 0
        """
        self.tbl[x][y] = 0

    def isset(self, x, y):
        """
        check if pos is already set
        """
        return self.get(x,y) == 1

    def inccnt(self):
        self.inc += 1

    def getinc(self):
        """
        get chess's edge size
        """
        return self.inc

    def isunique(self, row, col):
        """
        check if we put in (row,col),we can
        make sure the same line col duijiaoxian have no 1
        """
        size = self.size
        xais = [self.get(x,col) for x in range(size) if x != row]
        yais = [self.get(row,y) for y in range(size) if y != col]
        xyais = [self.get(x,y) for x in range(size) for y in range(size) if x - row == y - col]
        yxais = [self.get(x,y) for x in range(size) for y in range(size) if x - row == -y + col]
        if 1 in yais or 1 in xais or 1 in xyais or 1 in yxais:
            return False
        return True

    def show(self):
        for i in self.tbl:
            print i

def queen(tbl,lst):
    """
    param tbl: cheese table
    param lst: a list to store availiable queens,
                and output at last when success placed all
    """
    row = len(lst)
    if row == tbl.size: #we have all queens found, print out and continue find others
        tbl.inccnt()
        tbl.show()
        return 
    for i in range(tbl.size):

        if not tbl.isset(row, i) and  tbl.isunique(row, i):
            tbl.set(row, i)
            lst.append((row,i))
            queen(tbl,lst)
            lst.pop()
            tbl.unset(row,i)

#size = int(raw_input("how many rows? "))
#tbl = cheese(size)
#lst = []
#queen(tbl, lst)
#print "together",tbl.getinc()

def conflict(state, pos):
    num = len(state)
    for i in range(num):
        if abs(state[i] - pos) in (0, num - i):
            return True
    return False

def queues(num = 8, state = ()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num -1:
                yield (pos,)
            else:
                for result in queues(num, state + (pos,)):
                    yield (pos,) + result

def prettyprint(solution):
    def line(pos, length = len(solution)):
        return '.' * pos + 'X' + '.' * (length - pos - 1)
    for pos in solution:
        print line(pos)

prettyprint(random.choice(list(queues(8))))
#pprint.pprint(list(queues()))

