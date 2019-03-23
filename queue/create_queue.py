class Queue():
    """建立一个队列"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        # 返回队列是否为空
        return self.items == []

    def enqueue(self, item):
        # 队尾处入队列
        self.items.insert(0, item)

    def dequeue(self):
        # 队首出队列并返回值
        return self.items.pop()

    def size(self):
        # 返回当前队列大小
        return len(self.items)
