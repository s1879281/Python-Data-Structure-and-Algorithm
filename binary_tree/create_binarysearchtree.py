class TreeNode:
    """建立一个二叉树节点"""

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.payload
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc

        # 如果左右孩子不为None，则将该节点作为子节点的父节点
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def spliceOut(self):
        """继承节点的处理"""
        # 是叶节点，直接删除
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None

        # 有孩子，左孩子优先递补
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        """寻找后继节点"""
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        """找到该子树中键最小的节点"""
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current


class BinarySearchTree:
    """建立一棵二叉树"""

    def __init__(self):
        """初始化"""
        self.root = None
        self.size = 0

    def length(self):
        """返回二叉树的节点总数"""
        return self.size

    def __len__(self):
        """内置函数，返回二叉树的节点总数"""
        return self.size

    def __iter__(self):
        """返回根节点作为迭代对象"""
        return self.root.__iter__()

    def depth(self,node):
        """返回深度"""
        if node:
            return max(self.depth(node.leftChild),self.depth(node.rightChild))+1
        else:
            return 0

    def balanceFactor(self,node):
        return self.depth(node.leftChild)-self.depth(node.rightChild)

    def put(self, key, val):
        """插入一个节点"""
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        """在以当前节点为根节点的树中插入一个节点"""
        # 小则左，否则右。有孩则递归，无孩则插入
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
        else:
            currentNode.payload = val

    def __setitem__(self, k, v):
        """内置函数，插入一个节点"""
        self.put(k, v)

    def get(self, key):
        """查找一个节点"""
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        """在以当前节点为根节点的树中查找一个节点"""
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    def __getitem__(self, key):
        """内置函数，查找一个节点"""
        return self.get(key)

    def __contains__(self, key):
        """内置函数，判断是否包含某节点"""
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        """删除某个节点"""

        # 不是仅有根节点，用remove方法处理
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')

        # 仅有根节点
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        """内置函数，删除某个节点"""
        self.delete(key)

    def remove(self, currentNode):
        """删除指定节点"""
        # 叶节点，直接删除
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        # 有双子节点
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        # 只有一个子节点,孩子直接继承
        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


# mytree = BinarySearchTree()
# mytree[10] = 100
# mytree[5] = 50
# mytree[6] = 60
# mytree[13] = 130
# mytree[2] = 20
# mytree[2] = 20
# mytree[3] = 30
# print(mytree.root.payload)
# print(mytree.depth(mytree.root))
# print(mytree.depth(mytree.root.leftChild))
# print(mytree.depth(mytree.root.rightChild.rightChild))
# print(mytree.balanceFactor(mytree.root))
# del(mytree[5])
# print(mytree.root.payload)
# print('iter:')
# for i in mytree:
#     print(i)

