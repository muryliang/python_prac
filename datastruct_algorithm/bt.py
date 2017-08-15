import sys

class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, key):
        self.key = key

def consTree(lst):
    t = BinaryTree("")
    s = [] # used as a stack

    while len(lst) != 0:
        char = lst.pop(0)

        print (s)
        print ("char is", char)
        if char == "(":
            t.insertLeft("")
            s.append(t)
            t = t.getLeftChild()
        elif char == ")":
            t = s.pop()
        elif char in ['+','-','*','/','//','**']:
            t.setRootVal(char)
            t.insertRight("")
            s.append(t)
            t = t.getRightChild()
        elif char.isdigit():
            t.setRootVal(char)
            t = s.pop()
        else:
            raise Exception


if __name__ == "__main__":
    """implement a parse tree of full parathese calculation"""
    
    string = "( 3 + ( 4 * 5 ) )"
    t = consTree(string.split(" "))
