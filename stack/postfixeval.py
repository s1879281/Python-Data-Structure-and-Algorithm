from create_stack import Stack


def postfixEval(postfixexpr):
    """后缀表达式求值"""

    opstack = Stack()
    postfixList = postfixexpr.split()

    for symbol in postfixList:
        # 数字进栈，遇运算符，弹两个数字计算后压栈
        if ord(symbol) in range(48, 58):
            opstack.push(int(symbol))

        else:
            num2 = opstack.pop()
            num1 = opstack.pop()
            result = doMath(symbol, num1, num2)
            opstack.push(result)
    return opstack.pop()


def doMath(op, num1, num2):
    if op == "*":
        return num1 * num2
    if op == "/":
        return num1 / num2
    if op == "+":
        return num1 + num2
    else:
        return num1 - num2

print(postfixEval("7 4 + 3 4 5 * + *"))
