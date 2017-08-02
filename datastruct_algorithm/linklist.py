class Node():
    """one node in the linklist"""

    def __init__(self, item):
        self.item = item
        self.next = None

    def setNext(self, nextobj):
        self.next = nextobj

    def getNext(self):
        return self.next

    def getItem(self):
        return self.item

    def setItem(self, item):
        self.item = item

class List():
    """implementation of a linklist"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.setNext(self.head)
            self.head = node
        self.length += 1

    def remove(self, item):
        tmpnode = self.head
        while tmpnode is not None:
            if tmpnode.getItem() == item:
                self.length -= 1
                break

    def search(self, item):
        tmpnode = self.head
        while tmpnode is not None:
            if tmpnode.getItem() == item:
                return True
            tmpnode = tmpnode.getNext()
        return False

    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.length

    def append(self, item):
        node = Node(item)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.setNext(node)
        self.length += 1

    def index(self, item):
        tmpnode = self.head
        count = 0
        while tmpnode is not None:
            if tmpnode.getItem() == item:
                return count
            tmpnode = tmpnode.getNext()
            count += 1
        return -1

    def insert(self, pos, item):
        """assume position existence is enough"""
        node = Node(item)
        tmpnode = self.head
        if pos == 0: # if insert at first node pos, already done the size++
            self.add(item)
        else:
            for _ in range(pos-1):
                tmpnode = tmpnode.getNext()
            node.setNext(tmpnode.getNext())
            tmpnode.setNext(node)
            if self.length-1 == pos: # if insert at last node pos
                self.tail = node
            self.length += 1

    def pop(self):
        tmpnode = self.head
        while tmpnode.getNext() != self.tail:
            tmpnode = tmpnode.getNext()
        res = tmpnode.getNext()
        tmpnode.setNext(None)
        self.length -= 1
        return res

    def pop(self, pos):
        if pos == 0:
            res = self.head
            self.head = self.head.getNext()
            if self.length == 1:
                self.tail = None
        else:
            tmpnode = self.head
            for _ in range(pos-1):
                tmpnode = tmpnode.getNext()
            res = tmpnode.getNext()
            tmpnode.setNext(res.getNext())
            if pos == self.length-1:
                self.tail = tmpnode
        self.length -= 1
        return res



