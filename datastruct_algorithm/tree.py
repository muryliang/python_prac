class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.leftChild = None
        self.rightChild = None

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
    h[54] = 'cat'
    h[26] = 'dog'
    h[93] = 'lion'
    h[17] = 'tiger'
    h[77] = 'bird'
    h[31] = 'cow'
    h[44] = 'goat'
    h[55] = 'pig'
    h[20] = 'chicken'
    traverseInorder(h.head)
    print ()
    print (h[55], h[44])
    del h[55]
    traverseInorder(h.head)
    print ()
    del h[44]
    traverseInorder(h.head)
    print ()
    print ('bird' in h)
    print ('pig' in h)
    print ('goat' in h)
    del h[77]
    traverseInorder(h.head)
    print ()
