class inflist(object):
    def checkIndex(self, index):
        """
        check: 
        1. index of type int or long
        2. index >=0
        """
        if not isinstance(index, (int,long)):
            raise TypeError
        if index < 0:
            raise KeyError
    
    def __init__(self,start = 0, step = 1):
        self.changed = {}
        self.start = start
        self.step = step
        self.__size = 0

    def __getitem__(self, key):
        self.checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        self.checkIndex(key)
        self.changed[key] = value
        self.__size += 1

    def getSize(self):
        return self.__size

    def setSize(self, siz):
        self.__size = siz
    size = property(getSize, setSize)

    def __getattribute__(self, name):
            return super(inflist, self).__getattribute__( name)

    def __setattr__(self, name , value):
            super(inflist, self).__setattr__(name, value)

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a >= 10000:
            raise StopIteration
        return self.a

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    @classmethod
    def myclassmethod(cls, value):
        print "cls is ",cls
        print "value is ",value

    @staticmethod
    def mystaticmethod(value):
        print "this is static method"


if __name__ == "__main__":
    tmp = inflist()
#    print tmp[6],tmp[7],tmp[8]
    for i in tmp:
        print i
