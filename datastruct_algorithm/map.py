class Map():
    def __init__(self):
        self.size = 3
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.limit = self.size // 2

    def __len__(self):
        count = 0
        for i in range(self.size):
            if self.slots[i] != None:
                count += 1
        return count

    def __contains__(self, data):
        for i in range(self.size):
            if self.data[i] == data:
                return True
        return False


    def put(self, key, value):

        need_update = False
        slot = self.hashfunc(key, self.size)

        self.rehashcount = 1
        if self.slots[slot] == None:
            self.slots[slot] = key
            self.data[slot] = value
            if self.__len__() > self.limit:
                need_update = True
        else:
            if self.slots[slot] == key:
                self.data[slot] = value
            else:
                nextslot = self.rehash(slot, len(self.slots))
                while self.slots[nextslot] != None and  self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = value
                    if self.__len__() > self.limit:
                        need_update = True
                else:
                    self.data[nextslot] = value
        if need_update:
            self.increase((self.size+1)*2-1)

    def increase(self, size):
        origsize = self.size
        self.size = size
        self.limit = size // 2
        slots = self.slots
        self.slots = [None] * self.size
        data = self.data
        self.data = [None] * self.size
        for i in range(origsize):
            if slots[i] != None:
                self.put(slots[i], data[i])
        del slots
        del data
        self.size = size


    def __delitem__(self, key):
        startslot = self.hashfunc(key, self.size)
        position = startslot
        Found = False
        stop = False

        self.rehashcount = 1
        while not Found and not stop:
            if self.slots[position] == None:
                stop = True
            elif self.slots[position] == key:
                Found = True
                # first delete this
                print ("deleted", self.data[position])
                self.data[position] = None
                self.slots[position] = None
                # get the next position, until the origin one or None, reinsert them
                tmppos = self.rehash(position, self.size)
                while tmppos != startslot and self.slots[tmppos] != None:
                    tmpkey = self.slots[tmppos]
                    tmpdata = self.data[tmppos]
                    self.data[tmppos] = None
                    self.slots[tmppos] = None
                    self.put(tmpkey, tmpdata)
            else:
                position = self.rehash(position, self.size)
                if position == startslot: # this should test last ,because at start position == startslot
                    stop = True


    def hashfunc(self, key, size):
        return key%size

    def rehash(self, num, size):
        """qudratic probing"""

        res = (num+self.rehashcount**2)%size
        self.rehashcount += 1
#        res = (num + 1)%size
        return res

    def get(self, key):
        startslot = self.hashfunc(key, self.size)

        data = None
        stop = False
        found = False
        position = startslot
        self.rehashcount = 1
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.slots[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

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
    h[20] = 'duck'
    print (h.slots)
    print (h[55], h[44])
    del h[55]
    del h[44]
    print ('bird' in h)
    print ('pig' in h)
    print ('goat' in h)
