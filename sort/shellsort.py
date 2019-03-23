def shellsort(alist, gap):
    """希尔排序，将列表分为若干子列表，对每个子列表的同一个位置进行插入排序"""
    for startposition in range(0, gap):
        gapinsertsort(alist, startposition, gap)

    gapinsertsort(alist, 0, 1)


def gapinsertsort(alist, startposition, gap):
    """实现对不同startposition和指定gap的插入排序"""
    for index in range(startposition + gap, len(alist), gap):
        position = index
        currentvalue = alist[position]

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


a = [76, 43, 32, 54, 65, 13, 4, 5, 77]
shellsort(a, 4)
print(a)
