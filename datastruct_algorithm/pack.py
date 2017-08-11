def search(num, lst, reslist):
    if num <= 0 or len(lst) == 0:
        return 0
    value = 0
    if reslist.get(num,0) != 0:
        return reslist[num]

    for w, v in lst:
        tmplst = lst[:]
        tmplst.remove((w,v))
        if num >= w:
            curvalue = search(num - w, tmplst, reslist) + v
            if curvalue > value:
                value = curvalue
                reslist[num] = w
    return value

reslist = dict()
lst = [(2,3), (3,4), (4,8), (5,8), (9,10)]
search(20, lst, reslist)
num = 20

print (reslist)
while num != 0 and reslist.get(num, 0) != 0:
    print (reslist[num], end = " ")
    num -= reslist[num]
print ()
