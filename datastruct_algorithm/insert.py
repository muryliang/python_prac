def insert(lst):
    """every time compare to prev number ,if smaller, move that behind
    continue until foud a place

    cornercase: when compare to the left end
    """

    for i in range(1, len(lst)):
        tmps = lst[i]
        j = i
        while j -1 >= 0 and lst[j-1] > tmps:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = tmps

lst = [6,5,3,2,1]
insert(lst)
print (lst)
