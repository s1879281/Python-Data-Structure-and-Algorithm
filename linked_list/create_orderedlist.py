from create_node import Node


class OrderedList():
    """建立一个有序列表"""

    def __init__(self):
        self.head = None

    def isEmpty(self):
        # 返回链表是否为空
        return self.head == None

    def add(self, item):
        # 新增节点
        current = self.head
        previous=None
        stop = False
        while not stop and current != None:
            if current.getData() > item:
                stop = True
            else:
                previous=current
                current = current.getNext()
                
        temp = Node(item)
        if previous==None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        # 返回链表的节点数量
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        # 返回是否找到指定数值
        current = self.head
        found = False
        stop=False
        while not found and not stop and current != None:
            if current.getData() == item:
                found = True

            else:
                if current.getData()>item:
                    stop=True
                else:
                    current = current.getNext()

        return found

    def remove(self, item):
        # 删除指定值
        current = self.head
        previous = None
        found = False

        while not found and current != None:
            if current.getData() == item:
                found = True
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
            else:
                previous = current
                current = current.getNext()


mylist = UnorderedList()
mylist.add(14)
mylist.add(13)
mylist.add(13)
mylist.remove(13)
print(mylist.search(13))