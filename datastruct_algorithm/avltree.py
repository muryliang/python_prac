class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.size = 1 # means the max height of left and right +1,as leaf ,it is one

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size

    def getValue(self):
        return self.val

    def getKey(self):
        return self.key

    def setValue(self, value):
        self.val = value

    def setKey(self, key):
        self.key = key

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setLeftChild(self, val):
        self.leftChild = val

    def setRightChild(self, val):
        self.rightChild = val

    def cmpNode(self, item):
        """cmppare the node"""
        return self.cmpKey(item.getKey())

    def cmpKey(self, key):
        if self.key < key:
            return -1
        elif self.key == key:
            return 0
        else:
            return 1

    def rightRotate(self):
        """rotate cur node to right 
            and return the current root
        """
        assert self.leftChild != None
        left = self.leftChild
        self.leftChild = left.rightChild
        left.rightChild = self
        lsize = 0
        rsize = 0
        llsize = 0
        lrsize = 0
        if self.leftChild:
            lsize = self.leftChild.size
        if self.rightChild:
            rsize = self.rightChild.size
        if left.leftChild:
            llsize = left.leftChild.size
        self.size = 1 + max(lsize, rsize)
        left.size = 1 + max(llsize, self.size)
        return left

    def leftRotate(self):
        assert self.rightChild != None
        right = self.rightChild
        self.rightChild = right.leftChild
        right.leftChild = self
        lsize = 0
        rsize = 0
        rlsize = 0
        rrsize = 0
        if self.leftChild:
            lsize = self.leftChild.size
        if self.rightChild:
            rsize = self.rightChild.size
        if right.rightChild:
            rrsize = right.rightChild.size
        self.size = 1 + max(lsize, rsize)
        right.size = 1 + max(self.size, rrsize)
        return right

class Map:
    def __init__(self):
        self.size = 0
        self.head = None

    def __len__(self):
        return self.size

    def containKey(self, key):
        """use key's compare to determine the route to the key"""

        head = self.head
        while head != None:
            res = head.cmpKey(key)
            if res < 0:
                head = head.getRightChild()
            elif res > 0:
                head = head.getLeftChild()
            else:
                return True
        return False

    def __contains__(self, data):
        return self._search(self.head, data)

    def _search(self, head, data):
        if head == None:
            return False
        if head.getValue() == data:
            return True
        return  self._search(head.getLeftChild(), data) or self._search(head.getRightChild(), data)

    def put(self, key, value):
        self.head = self._insert(self.head, key, value)

    def _insert(self, root, key, value):
        """recursively insert or update if exist"""

        if root == None:
            self.size += 1
            return Node(key, value)
        else:
            res = root.cmpKey(key)
            if res < 0:
                root.setRightChild(self._insert(root.getRightChild(), key, value))
            elif res > 0:
                root.setLeftChild(self._insert(root.getLeftChild(), key, value))
            else: # res == 0
                root.setValue(value)
            root = self._sizeBalance(root)
            return root

    def _sizeBalance(self, root):
        """process four type of rotate here, combined by left rotate and right rotate"""

        lsize = 0
        rsize = 0
        if root.getLeftChild():
            lsize = root.getLeftChild().getSize()
        if root.getRightChild():
            rsize = root.getRightChild().getSize()
        root.setSize(1 + max(lsize, rsize))

        # balance size
        if lsize - rsize >= 2:
            if root.getLeftChild().getLeftChild() == None: # left-right type
                root.setLeftChild(root.getLeftChild().leftRotate())
            root = root.rightRotate() #left-left && left-right type
        elif lsize - rsize <= -2:
            if root.getRightChild().getRightChild() == None: #right-left type
                root.setRightChild(root.getRightChild().rightRotate())
            root = root.leftRotate()
        return root

    def _findMin(self, root):
        while root.getLeftChild() != None:
            root = root.getLeftChild()
        return root

    def __delitem__(self, key):
        if self.head != None:
            self.head = self._delete(self.head, key)

    def _delete(self, root, key):
        if root == None:
            # when you are deleteing a non-existence one
            return None
        res = root.cmpKey(key)
        if res < 0:
            root.setRightChild(self._delete(root.getRightChild(), key))
        elif res > 0:
            root.setLeftChild(self._delete(root.getLeftChild(), key))
        else: # res == 0
            if root.getLeftChild() == None:
                return root.getRightChild()
            elif root.getRightChild() == None:
                return root.getLeftChild()
            else:
                leftMin = self._findMin(root.getRightChild())
                root.setRightChild(self._delete(root.getRightChild(), leftMin.getKey()))
                leftMin.setLeftChild(root.getLeftChild())
                leftMin.setRightChild(root.getRightChild())
                root = leftMin
            self.size -= 1
        root = self._sizeBalance(root)
        return root

    def get(self, key):
        root = self.head
        while root != None:
            res = root.cmpKey(key)
            if res < 0:
                root = root.getRightChild()
            elif res > 0:
                root = root.getLeftChild()
            else:
                return root.getValue()
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

def traverseInorder(tree):
    if tree == None:
        return
    traverseInorder(tree.getLeftChild())
    print (tree.getKey(), tree.getValue(), end=" ")
    traverseInorder(tree.getRightChild())

if __name__ == "__main__":
    h = Map()
    h[1] = 'cat'
    h[2] = 'dog'
    h[3] = 'lion'
    h[4] = 'tiger'
    h[5] = 'bird'
    h[6] = 'cow'
    h[7] = 'goat'
    h[8] = 'pig'
    h[9] = 'chicken'
    traverseInorder(h.head)
    print (h.head.size)
