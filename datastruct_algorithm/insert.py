def insert(lst):
    insertInto(lst, 0, len(lst)-1)

def insertInto(lst, lo, hi):
    """every time compare to prev number ,if smaller, move that behind
    continue until foud a place

    cornercase: when compare to the left end
    """

    for i in range(lo+1, hi-lo+1):
        tmps = lst[i]
        j = i
        while j -1 >= 0 and lst[j-1] > tmps:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = tmps

if __name__ == "__main__":
    lst = [6,5,3,2,1]
    insert(lst)
    print (lst)
