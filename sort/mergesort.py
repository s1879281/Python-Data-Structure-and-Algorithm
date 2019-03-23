import time

def mergesort(alist):
    """归并排序"""
    # 对长度大于1的列表执行排序，否则直接返回原列表
    print("对该列表排序：", alist)
    if len(alist) > 1:
        middle = len(alist) // 2
        # 对两个切片进行归并排序
        lefthalf = mergesort(alist[:middle])
        righthalf = mergesort(alist[middle:])

        i = 0
        j = 0
        alist = []
        # 左列表和右列表最小值比较，较小值添加进新列表
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist.append(lefthalf[i])
                i += 1
            else:
                alist.append(righthalf[j])
                j += 1
        # 左列表和右列表剩余值添加进新列表
        while i < len(lefthalf):
            alist.append(lefthalf[i])
            i += 1

        while j < len(righthalf):
            alist.append(righthalf[j])
            j += 1

        print("对该列表排序后：", alist)
    return alist

def mergesort_modified(alist,start,end):
    """不用切片的归并排序"""
    # 对长度大于1的列表执行排序，否则直接返回原列表
    print("对该列表排序：", alist[start:end+1])
    if end-start > 0:
        middle = (end+start+1) // 2
        # 对两个切片进行归并排序
        mergesort_modified(alist,start,middle-1)
        mergesort_modified(alist,middle,end)

        i = start
        j = middle
        newlist=[]
        # 左列表和右列表最小值比较，较小值添加进新列表
        while i <= middle-1 and j <= end:
            if alist[i] <= alist[j]:
                newlist.append(alist[i])
                i += 1
            else:
                newlist.append(alist[j])
                j += 1
        # 左列表和右列表剩余值添加进新列表
        while i <= middle-1:
            newlist.append(alist[i])
            i += 1

        while j <= end:
            newlist.append(alist[j])
            j += 1
        alist[start:end+1]=newlist
        print("对该列表排序后：", alist[start:end+1])

a = [78, 51, 77, 32, 88, 66, 1]

start1=time.time()
for i in range(10000):
    b = mergesort(a)
end1=time.time()

start2=time.time()
for i in range(10000):
    mergesort_modified(a,0,len(a)-1)
end2=time.time()

print(end1-start1,end2-start2)