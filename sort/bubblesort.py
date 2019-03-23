def bubblesort(alist):
    """冒泡排序"""
    for passnum in range(len(alist) - 1):
        for i in range(len(alist) - passnum - 1):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


def short_bubblesort(alist):
    """短冒泡排序，一次遍历没有排序即停止"""
    stop = False

    for passnum in range(len(alist) - 1):
        # 如果一次遍历中有发生交换，stop置为False，否则程序终止
        if stop == True:
            break
        stop = True
        for i in range(len(alist) - passnum - 1):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                stop = False


a = [4, 3, 5, 7, 1, 3, 6]
bubblesort(a)
b = [7, 6, 4, 5, 3, 1, 2]
short_bubblesort(b)
print(a)
print(b)
