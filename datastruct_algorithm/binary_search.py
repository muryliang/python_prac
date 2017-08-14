def bin(lst, num):
    """binary search implementation

    lst: the list
    num: the number to be found
    """

    lo = 0
    hi = len(lst)-1

    while hi >= lo:
        mid = lo + (hi - lo) // 2
        if lst[mid] > num:
            hi = mid - 1
        elif lst[mid] < num:
            lo = mid + 1
        else:
            return True
    return False

lst = [2,3,5,6,8,9,11,14]
num = 11
print (bin(lst, num))

