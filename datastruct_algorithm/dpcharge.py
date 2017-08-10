def dpcharge(clist, num, coindict, last):
    # for every coin less than num 
    for cent in range(num+1):
        coincount = cent
        newcoin = 1
        for i in [c for c in clist if c <= cent]:
            coinnumber = coindict.get(cent - i, 0) + 1
            if coinnumber < coincount:
                coincount = coinnumber
                newcoin = i
        coindict[cent] = coincount
        last[cent] = newcoin
    return coindict[num]

num = int(input("input number: "))
last = dict()
print(dpcharge([1,5,8,10,25], num, dict(), last))
while num != 0:
    print (last[num], end=" ")
    num -= last[num]

