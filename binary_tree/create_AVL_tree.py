from create_binarysearchtree import TreeNode, BinarySearchTree


class AVL_Tree(BinarySearchTree):
    """建立AVL树，为BST树的子类"""

    def __init__(self):
        """继承"""
        super().__init__()

    def _put(self, key, val, currentNode):
        """重写插入节点方法"""
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode)

    def updateBalance(self, node):
        """向上查每个节点是否平衡，更新一次后则停止"""
        if self.balanceFactor(node) > 1 or self.balanceFactor(node) < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if self.balanceFactor(node.parent) != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
        """左旋"""
        # 树立新根
        newRoot = rotRoot.rightChild

        # 孩子的交接
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot

        # 父母的交接
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot

        # 新旧根节点的关系转变
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot

    def rotateRight(self, rotRoot):
        """右旋"""
        # 树立新根
        newRoot = rotRoot.leftChild

        # 孩子的交接
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot

        # 父母的交接
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot

        # 新旧根节点的关系转变
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot

    def rebalance(self, node):
        """右旋查左，保证左边重；左旋查右，保证右边重"""
        if self.balanceFactor(node) < 0:
            if self.balanceFactor(node.rightChild) > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        else:
            if self.balanceFactor(node.leftChild) < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

mytree = AVL_Tree()
mytree[10] = 100
mytree[5] = 50
mytree[6] = 60
print(mytree.root.payload)
for i in mytree:
    print(i)
