def quicksort(alist):
    """快速排序"""
    quicksorthelper(alist, 0, len(alist) - 1)


def quicksorthelper(alist, first, last):
    """递归实现，将枢轴点两侧列表分别进行快速排序"""
    if first < last:
        splitpoint = partition(alist, first, last)

        quicksorthelper(alist, first, splitpoint - 1)
        quicksorthelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    """返回枢轴点，并使枢轴点左侧的值均小于枢轴点，右侧均大于枢轴点"""
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True

        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


alist = [43, 21, 54, 67, 23, 65, 32]
quicksort(alist)
print(alist)
