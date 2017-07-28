class Queue():
    """this is a queue implementation using list
    """
    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.insert(0, item)

    def dequeue(self):
        return self.q.pop()

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.q)

if __name__ == "__main__":
    q = Queue()
    print (q.isEmpty())
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print (q.size())
    print (q.isEmpty())
    q.enqueue(8.4)
    print (q.dequeue())
    print (q.dequeue())
    print (q.size())
