def swap(a,b):
    """交换顺序"""
    a=a+b
    b=a-b
    a=a-b
    return a,b

def selectionsort(alist):
    """选择排序，即每次遍历只找出最大的值，与遍历值中的最后一位交换"""
    for passnum in range(len(alist),1,-1):
        maxindex=0
        for i in range(0,passnum):
            if alist[i]>alist[maxindex]:
                maxindex=i
        if maxindex<passnum-1:
            alist[passnum-1],alist[maxindex]=swap(alist[passnum-1],alist[maxindex])


a=[5,6,7,8,3,2,1,0]
selectionsort(a)
print(a)
