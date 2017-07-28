class Stack():
    """this is a stack implementing using list
    """
    def __init__(self):
        self.stk = []

    def push(self, item):
        self.stk.append(item)

    def pop(self):
        return self.stk.pop()

    def peek(self):
        return self.stk[-1]

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.stk)

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count < self.size():
            res = self.stk[self.count]
            self.count += 1
            return res
        else:
            raise StopIteration

    def __str__(self):
        return str(self.stk)

if __name__ == "__main__":
    s = Stack()
    s.push(4)
    s.push('dog')
    print (s.peek())
    s.push(True)
    print (s.size())
    print (s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
    print ("remaining:")
    for i in s:
        print (i, end=" ")
    print ()
    print ("s is:")
    print (s)
