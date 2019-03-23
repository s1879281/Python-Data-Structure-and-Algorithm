class Hashtable():
    """建立一个哈希表"""

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        """将key和data值对添加到哈希表中"""
        hashvalue = self.hashfunction(key, len(self.slots))
        searched=[]

        while self.slots[hashvalue] != None and self.slots[hashvalue] != key and len(searched)< len(self.slots):
            if hashvalue not in searched:
                searched.append(hashvalue)
            hashvalue = self.rehash(hashvalue, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        elif self.slots[hashvalue] ==key:
            self.data[hashvalue] = data
        else:
            print("no empty slots")

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def get(self, key):
        """从哈希表中获得值"""
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


def main():

    hash=Hashtable()
    hash[55]=121
    hash[66]=133
    hash[2]=133
    hash[3]=133
    hash[4]=133
    hash[5]=133
    hash[6]=133
    hash[7]=133
    hash[8]=133
    hash[9]=133
    hash[10]=133
    hash[10]=133
    hash[20]=133
    print(hash.slots)
    print(hash.data)


main()