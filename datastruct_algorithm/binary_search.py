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

def bin2(lst, num):
    return subbin2(lst, 0, len(lst)-1, num)

def subbin2(lst, lo, hi, num):
    if lo > hi:
        return False
    mid = (lo + hi) // 2
    if lst[mid] < num:
        return subbin2(lst, mid + 1, hi, num)
    elif lst[mid] > num:
        return subbin2(lst, lo, mid-1, num)
    else:
        return True

lst = [2,3,5,6,8,9,11,14]
num = 13
print (bin2(lst, num))

