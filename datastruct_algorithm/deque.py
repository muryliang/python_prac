class Deque():
    """this is an implementation of deque"""

    def __init__(self):
        self.dq = []

    def addFront(self, item):
        self.dq.append(item)

    def addRear(self, item):
        self.dq.insert(0, item)

    def removeFront(self):
        return self.dq.pop()

    def removeRear(self):
        return self.dq.pop(0)

    def isEmpty(self):
        return len(self.dq) == 0

    def size(self):
        return len(self.dq)

if __name__ == "__main__":
    d = Deque()
    assert d.isEmpty() == True
    d.addRear(4)
    d.addRear('dog')
    d.addFront('cat')
    d.addFront(True)
    print (d.size())
    print (d.isEmpty())
    d.addRear(8.4)
    print(d.removeRear())
    print (d.removeFront())
    print (d.dq)

