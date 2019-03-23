import operator

from create_binarytree import Binarytree
from create_stack import Stack


def buildparsetree(mathexp):
    """建立分析树，使用了栈和二叉树数据结构"""
    fplist = mathexp.split()
    pstack = Stack()
    etree = Binarytree('')
    pstack.push(etree)
    currenttree = etree

    for i in fplist:
        if i == '(':
            # 压栈，并使左孩子为当前操作节点
            currenttree.insertleft('')
            pstack.push(currenttree)
            currenttree = currenttree.getleftchild()
        elif i not in ['+', '-', '*', '/', ')']:
            # 在当前节点设操作数，并使父节点弹栈并成为当前操作节点
            currenttree.setrootval(int(i))
            parent = pstack.pop()
            currenttree = parent
        elif i in ['+', '-', '*', '/']:
            # 在当前节点设操作符，压栈，并使右孩子为当前操作节点
            currenttree.setrootval(i)
            currenttree.insertright('')
            pstack.push(currenttree)
            currenttree = currenttree.getrightchild()
        elif i == ')':
            # 弹栈
            currenttree = pstack.pop()
        else:
            raise ValueError
    return etree


def postorder(parsetree):
    """后序遍历"""
    if parsetree != None:
        postorder(parsetree.getleftchild())
        postorder(parsetree.getrightchild())
        print(parsetree.getrootval())


def evaluate(parsetree):
    """通过递归运算，运算符为根节点，操作数为叶节点"""
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    leftC = parsetree.getleftchild()
    rightC = parsetree.getrightchild()

    if leftC and rightC:
        fn = opers[parsetree.getrootval()]
        return fn(evaluate(leftC), evaluate(rightC))

    else:
        return parsetree.getrootval()


pt = buildparsetree('( 3 + ( 4 * 5 ) )')
postorder(pt)
print(evaluate(pt))
