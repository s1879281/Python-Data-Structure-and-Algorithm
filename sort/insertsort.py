def insertsort(alist):
    """插入排序，从第二个数字开始，往前面已经排好序的列表中插入"""
    for index in range(1,len(alist)):
        currentvalue=alist[index]
        position=index

        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position=position-1
        alist[position]=currentvalue

a=[32,55,32,65,76,12,13]
insertsort(a)
print(a)