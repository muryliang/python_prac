def bb(lst):
    n = len(lst)
    exchange = True
    for i in range(n-1, 0, -1):
        if exchange is False:
            break
        exchange = False
        for j in range(0, i):
            if lst[j] > lst[j+1]:
                exchange = True
                lst[j], lst[j+1] = lst[j+1], lst[j]

def bb2(lst):
    state = True #up 0 for down
    n = len(lst)
    exchange = True
    lo = 0
    hi = n-1
    while lo <= hi:
#    for i in range(n-1, lo, -1):
        if exchange is False:
            break
        exchange = False
        if state == True:
            print ("one", lo, hi)
            for j in range(lo, hi):
                if lst[j] > lst[j+1]:
                    exchange = True
                    lst[j], lst[j+1] = lst[j+1], lst[j]
            state = not state
            hi -= 1
            print (lst)
        else:
            print ("two", lo, hi)
            for j in range(hi, lo, -1):
                if lst[j] < lst[j-1]:
                    exchange = True
                    lst[j], lst[j-1] = lst[j-1], lst[j]
            lo += 1
            state = not state
            print (lst)
lst = [7,6,5,4,3,2,1]
bb2(lst)
#print (lst)
