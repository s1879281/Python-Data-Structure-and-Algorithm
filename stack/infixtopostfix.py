from create_stack import Stack


def infixToPostfix(infixexpr):
    """中缀表达式转化为后缀表达式"""
    # 建立栈
    opstack = Stack()

    # 建立优先级字典
    prio = {}
    prio["*"] = 3
    prio["/"] = 3
    prio["+"] = 2
    prio["-"] = 2
    prio["("] = 1

    postfixList = []
    infixList = infixexpr.split()

    for symbol in infixList:
        # 数字直接入队列
        if ord(symbol) in range(65, 91) or ord(symbol) in range(48, 58):
            postfixList.append(symbol)

        # 左括号入栈
        elif symbol == '(':
            opstack.push(symbol)

        # 右括号从栈顶弹栈，直到左括号弹出
        elif symbol == ')':
            topsymbol = opstack.pop()
            while topsymbol != '(':
                postfixList.append(topsymbol)
                topsymbol = opstack.pop()

        # 栈顶优先则弹，然后入栈
        else:
            while (not opstack.isEmpty()) and prio[opstack.peek()] >= prio[symbol]:
                postfixList.append(opstack.pop())
            opstack.push(symbol)

    # 按顺序弹出栈内剩余符号
    while not opstack.isEmpty():
        postfixList.append(opstack.pop())
    return "".join(postfixList)


print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( X + Y ) * ( A + B * C ) + M * N"))
print(infixToPostfix("3 + 5 * 6"))
