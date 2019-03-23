import time

def recmc(coninvaluelist, change):
    """找零问题，递归，速度慢"""
    mincoins = change
    if change in coninvaluelist:
        return 1
    else:
        for i in [c for c in coninvaluelist if c <= change]:
            numcoins = 1 + recmc(coninvaluelist, change - i)
            if numcoins < mincoins:
                mincoins = numcoins
    return mincoins


def recDC(coinValueList, change, knownResults):
    """记忆化搜索，递归"""
    mincoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numcoins = 1 + recDC(coinValueList, change - i, knownResults)
            if numcoins < mincoins:
                mincoins = numcoins
                knownResults[change] = mincoins
    return mincoins


def dpmakechange(coinvaluelist, change, mincoins):
    """动态规划，从小到大计算每个change需要的币数"""
    for cents in range(change + 1):
        coincount = cents
        for j in [c for c in coinvaluelist if c <= cents]:
            if mincoins[cents - j] + 1 < coincount:
                coincount = mincoins[cents - j] + 1
        mincoins[cents] = coincount
    return mincoins[change]



def timer(n,func):
    start=time.time()
    for i in range(n):
        func()
    end=time.time()

    return end-start

def main1():
    amnt = 11
    clist = [1, 5, 10, 21, 25]
    coincount = [0] * (amnt + 1)
    recDC(clist, amnt, coincount)

def main2():
    amnt = 11
    clist = [1, 5, 10, 21, 25]
    coincount = [0] * (amnt + 1)
    dpmakechange(clist, amnt, coincount)

print(timer(100000,main1))
print(timer(100000,main2))


