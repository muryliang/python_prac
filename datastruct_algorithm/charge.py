coin = [1,5,10,25]
calls = 0
def charge(coin, num, res):
    global calls
    calls += 1
    mincoin = num
    if num in coin:
        res[num] = 1
        return 1
    elif res.get(num, 0) != 0:
        return res[num]

    for i in [c for c in coin if c <= num]:
        numcoins = 1 + charge(coin, num - i, res)
        if numcoins < mincoin:
            mincoin = numcoins
            res[num] = mincoin
    return mincoin

num = charge(coin, int(input("you charge coin: ")), dict())
print ("the number is %d, calls %d"%(num, calls))

