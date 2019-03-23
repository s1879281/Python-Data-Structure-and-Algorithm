class Stack():
    """建立一个栈"""
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        # 返回是否为空
        return self.items==[]

    def push(self,item):
        # 入栈
        self.items.append(item)

    def pop(self):
        # 出栈并返回出栈数据
        return self.items.pop()

    def peek(self):
        # 返回栈顶数据
        return self.items[len(self.items)-1]

    def size(self):
        # 返回当前栈大小
        return len(self.items)
