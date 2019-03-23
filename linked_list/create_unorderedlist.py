from create_node import Node

class UnorderedList():
    """建立一个无序列表"""
    def __init__(self):
        self.head=None

    def isEmpty(self):
        # 返回链表是否为空
        return self.head==None

    def add(self,item):
        # 新增节点(头插法)
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp

    def size(self):
        # 返回链表的节点数量
        current=self.head
        count=0
        while current!=None:
            count=count+1
            current=current.getNext()

        return count

    def search(self,item):
        # 返回是否找到指定数值
        current=self.head
        found=False
        while not found and current!=None:
            if current.getData()==item:
                found=True

            else:
                current=current.getNext()

        return found

    def remove(self,item):
        # 删除指定值
        current=self.head
        previous=None
        found =False

        while not found and current!=None:
            if current.getData()==item:
                found=True
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
            else:
                previous=current
                current=current.getNext()



mylist=UnorderedList()
mylist.add(14)
mylist.add(13)
mylist.add(13)
mylist.remove(13)
print(mylist.search(13))