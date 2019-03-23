class BinaryTree:
    """建立一棵二叉树"""

    def __init__(self, rootObj):
        """初始化根节点值，左子树，右子树"""
        self.key = rootObj
        self.leftchild = None
        self.rightchild = None

    def insertleft(self, newNode):
        """如果左子树为空，则将新节点插入为左子树；如果左子树不为空，则将原左子树作为新节点的左子树，新节点作为新左子树"""
        if self.leftchild == None:
            self.leftchild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.leftchild = self.leftchild
            self.leftchild = t

    def insertright(self, newNode):
        """如果右子树为空，则将新节点插入为右子树；如果右子树不为空，则将原右子树作为新节点的右子树，新节点作为新右子树"""
        if self.rightchild == None:
            self.rightchild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.rightchild = self.rightchild
            self.rightchild = t

    def getrightchild(self):
        """返回左子树"""
        return self.rightchild

    def getleftchild(self):
        """返回右子树"""
        return self.leftchild

    def setrootval(self, obj):
        """获取根节点的值"""
        self.key = obj

    def getrootval(self):
        """重设根节点的值"""
        return self.key

    def preorder(self):
        """前序遍历"""
        print(self.key)
        if self.leftchild:
            self.leftchild.preorder()
        if self.rightchild:
            self.rightchild.preorder()

    def postorder(self):
        """后序遍历"""
        if self.leftchild:
            self.leftchild.postorder()
        if self.rightchild:
            self.rightchild.postorder()
        print(self.key)

    def inorder(self):
        """中序遍历"""
        if self.leftchild:
            self.leftchild.inorder()
        print(self.key)
        if self.rightchild:
            self.rightchild.inorder()
