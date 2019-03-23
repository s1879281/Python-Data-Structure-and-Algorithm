def sequentialsearch(alist,item):
    """顺序查找。复杂度为 O（n）"""
    pos=0
    found=False

    while pos <len(alist) and not found:
        if alist[pos]==item:
            found=True

        else:
            pos=pos+1

    return found


testlist=[1,5,7,9]
print(sequentialsearch(testlist,5))
print(sequentialsearch(testlist,13))