def binarysearch(alist, item):
    """二分查找,适用于顺序列表,复杂度 O(log n)"""
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True

        elif alist[midpoint] > item:
            last = midpoint - 1

        else:
            first = midpoint + 1

    return found


def binarysearch_recursion(alist, item):
    """二分递归查找, 传递切片, 效率略低"""
    if len(alist) == 0:
        return False

    else:
        midpoint = len(alist) // 2

        if alist[midpoint] == item:
            return True

        elif alist[midpoint] > item:
            return binarysearch_recursion(alist[:midpoint], item)

        else:
            return binarysearch_recursion(alist[midpoint + 1:], item)


testlist = [1, 5, 7, 9, 13, 16, 17, 18]
print(binarysearch(testlist, 5))
print(binarysearch(testlist, 12))
print(binarysearch_recursion(testlist, 7))
