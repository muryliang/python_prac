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

lst = [6,5,4,3,2,1]
bb(lst)
print (lst)
