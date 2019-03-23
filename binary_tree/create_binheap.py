class Binheap:
    """建立一个二叉堆"""

    def __init__(self):
        self.heaplist = [0]
        self.currentsize = 0

    def percup(self, i):
        """比较与父节点的大小，若小于父节点，则与父节点交换"""
        while i // 2 > 0:
            if self.heaplist[i] < self.heaplist[i // 2]:
                tmp = self.heaplist[i // 2]
                self.heaplist[i // 2] = self.heaplist[i]
                self.heaplist[i] = tmp
            i = i // 2

    def insert(self, k):
        """插入新值"""
        self.heaplist.append(k)
        self.currentsize = self.currentsize + 1
        self.percup(self.currentsize)

    def percdown(self, i):
        """比较与较小的子节点的大小，若大于较小的子节点，则与之交换"""
        while i * 2 <= self.currentsize:
            mc = self.minChild(i)
            if self.heaplist[i] > self.heaplist[mc]:
                tmp = self.heaplist[i]
                self.heaplist[i] = self.heaplist[mc]
                self.heaplist[mc] = tmp
            i = mc

    def minChild(self, i):
        """返回较小的子节点"""
        if i * 2 + 1 > self.currentsize:
            return i * 2
        else:
            if self.heaplist[i * 2] < self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delmin(self):
        """返回最小值，将末尾值放在根节点，然后重新构建堆"""
        retval = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.currentsize]
        self.currentsize = self.currentsize - 1
        self.heaplist.pop()
        self.percdown(1)
        return retval

    def buildheap(self, alist):
        """现有列表构建二叉堆"""
        i = len(alist) // 2
        self.currentsize = len(alist)
        self.heaplist = [0] + alist[:]
        while i > 0:
            self.percdown(i)
            i = i - 1
