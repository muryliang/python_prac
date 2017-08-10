def traverse(head):
    while head is not None:
        print (head.val, end=" ")
        head = head.getNext()
    print()

def rlist(lst):
    if len(lst) <= 1:
        return lst
    return lst[-1:] + rlist(lst[:-1])

def reverseList(head):
    if head is None:
        return None
    if head.getNext() is None: #base case 
        return head
    tmphead = reverseList(head.getNext())
    curhead = tmphead
    while tmphead.getNext() is not None:
        tmphead = tmphead.getNext()
    tmphead.setNext(head)
    head.setNext(None)
    return curhead

class Node():
    def __init__(self, val, nex=None):
        self.val = val
        self.nex = nex

    def setNext(self, nex):
        self.nex = nex

    def getNext(self):
        return self.nex



if __name__ == "__main__":
    num = int(input("input your range: "))
    head = None
    for i in range(num):
        node = Node(i)
        if head is None:
            head = node
        else:
            node.setNext(head)
            head = node
    traverse(head)
    head = reverseList(head)
    traverse(head)
