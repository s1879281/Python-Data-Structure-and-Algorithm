from create_deque import Deque

def palchecker(aString):
    """回文检查"""
    chardeque=Deque()

    for char in aString:
        chardeque.addRear(char)

    stillEqual=True

    # 检查首尾字符是否一致
    while chardeque.size()>1 and stillEqual:
        first=chardeque.removeFront()
        last=chardeque.removeRear()
        if first!=last:
            stillEqual=False

    return stillEqual

print(palchecker('lsdkkdsl'))
print(palchecker('lsdkdsl'))
print(palchecker('ldsl'))

