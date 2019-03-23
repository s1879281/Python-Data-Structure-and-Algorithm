from create_stack import Stack


def baseConverter(number, base):
    """将十进制数转化为其他进制"""

    s = Stack()

    while number > 0:
        # 除以base后余数入栈
        rem = number % base
        s.push(rem)
        number = number // base

    string = ""
    while not s.isEmpty():
        string = string + str(s.pop())
    return string


print(baseConverter(3, 2))
print(baseConverter(100, 8))
