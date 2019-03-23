from create_stack import Stack


def parChecker(symbolString):
    """判断一个括号字符串是否左右对等"""

    s = Stack()

    for index in range(len(symbolString)):
        # 左括号入栈
        if symbolString[index] == '(':
            s.push('(')

        # 右括号先检查是否空栈，否则栈顶左括号出栈
        else:
            if s.isEmpty() == True:
                return False
            else:
                s.pop()

    if s.isEmpty() == True:
        return True

    else:
        return False


print(parChecker("()()()"))
print(parChecker("()())"))
print(parChecker("(()())"))
