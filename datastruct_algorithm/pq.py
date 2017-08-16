class BinaryHeap:
    """ a min heap"""

    def __init__(self):
        self.q = [None]
        self.count = 0

    def insert(self, key):
        self.q.append(key)
        self.swimUp(len(self.q)-1)

    def swimUp(self, idx):
        while idx != 1:
            if self.q[idx] < self.q[idx//2]:
                self.q[idx], self.q[idx//2] = self.q[idx//2], self.q[idx]
            idx //= 2

    def diveDown(self, idx):
        while 2 * idx < len(self.q):
            tmp = 2*idx
            if 2 * idx + 1 < len(self.q) and self.q[2*idx+1] < self.q[2*idx]:
                tmp = 2*idx+1
            if self.q[tmp] < self.q[idx]:
                self.q[tmp], self.q[idx] = self.q[idx], self.q[tmp]
            idx = tmp

    def findMin(self):
        if len(self.q) >= 2:
            return self.q[1]
        else:
            return None

    def delMin(self):
        """ here we use dynamic list, so deal with corner case of no item

        if we use an abstract list, we can just use self.q[1] = last
        and extra self.size to make judge
        """
        if len(self.q) == 1:
            return None
        res = self.q[1]
        last = self.q.pop()
        if len(self.q) != 1:
            self.q[1] = last
        else:
            self.q.append(last)
        self.diveDown(1)
        return res

    def isEmpty(self):
        return len(self.q) == 1

    def size(self):
        return len(self.q) -1

    def buildHeap(self, lst):
        while len(lst) != 0:
            self.insert(lst.pop())


if __name__ == "__main__":
    bh = BinaryHeap()
    bh.insert(5)
    print (bh.q)
    bh.insert(7)
    print (bh.q)
    bh.insert(3)
    print (bh.q)
    bh.insert(11)
    print (bh.q)

    print (bh.delMin())
    print (bh.q)
    print (bh.delMin())
    print (bh.q)
    print (bh.delMin())
    print (bh.q)
    print (bh.delMin())
    print (bh.q)
