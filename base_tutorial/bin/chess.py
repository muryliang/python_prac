#/usr/bin/python2
import os

__metaclass__ = type
class Chess(object):
    def init(self, row):
        "initialize a chess table"
        self.table = [[0] * row for i in range(row)]
        self.len = row

    def show(self):
        "show the chess table"
        print "table:"
        for i in self.table:
            print i

    def set(self, row, col):
        "set a pos on table"
        if row in range(self.len) and col in range(self.len):
            self.table[row][col] = 1
        else:
            print "out of range!"

        
while True:
    try:
        row = int(raw_input("how many row? "))
    except Exception,e:
        print e
        print "I need an integer"
    else:
        break;

chess = Chess()
chess.init(row)
chess.show()

while  True:
    try:
        pos = raw_input("pos: ")
        x,y = [int(k) for k in pos.split()]
        assert x in range(row) and y in range(row)
        chess.set(x,y)
        os.system('clear')
        chess.show()
    except (Exception,KeyboardInterrupt),e:
        print  e, "Try again"
