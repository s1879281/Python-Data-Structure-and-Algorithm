def toStr(number,base):
    """十进制数到任意进制的字符转换"""
    convertString="0123456789ABCDEF"

    if number<base:
        return convertString[number]

    return toStr(number//base,base)+convertString[number%base]

print(toStr(3,2))
print(toStr(100,8))
print(toStr(31,16))