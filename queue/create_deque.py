class Deque:
    """建立一个双端队列"""

    def __init__(self):
        self.items=[]

    def isEmpty(self):
        # 返回是否为空
        return self.items==[]

    def addFront(self,item):
        # 队首新增数据
        self.items.append(item)

    def addRear(self,item):
        # 队尾新增数据
        self.items.insert(0,item)

    def removeFront(self):
        # 队首删除数据
        return self.items.pop()

    def removeRear(self):
        # 队尾删除数据
        return self.items.pop(0)

    def size(self):
        return len(self.items)