import insert

"""this version not optimized for duplicate"""

def quick(lst):
    qsort(lst, 0, len(lst)-1)

def midOfThree(lst, lo, hi):
    mid = (lo + hi) // 2
    if lst[lo] <= lst[mid]:
        if lst[mid] <= lst[hi]:
            return mid
        elif lst[lo] <= lst[hi]:
            return hi
        else:
            return lo
    else: # lo > mid
        if lst[mid] > lst[hi]:
            return mid
        elif lst[lo] > lst[hi]:
            return hi
        else:
            return lo

def split(lst, lo, hi):
    """everything before(not inclusive) lt is less than to sample, everything after
    gt is  greater than sample, [lt, gt] are equals
    """

#    idx = midOfThree(lst, lo, hi)
#    lst[lo], lst[idx] = lst[idx], lst[lo]

    sample = lst[lo]
    i = lo
    lt = lo
    gt = hi
    done = False

    while not done:
        while i <= gt and lst[i] == sample:
            i += 1

        if i > gt:
            done = True

        elif lst[i] < sample:
            lst[i], lst[lt] = lst[lt], lst[i]
            i += 1
            lt += 1
        elif lst[i] > sample:
            lst[i], lst[gt] = lst[gt], lst[i]
            gt -= 1

    return lt, gt

def qsort(lst, lo, hi):
    limit = 13
    if hi > lo:
        if hi - lo < limit:
            insert.insertInto(lst, lo, hi)
        lt, gt = split(lst, lo, hi)

        qsort(lst, lo, lt-1)
        qsort(lst, gt+1, hi)

if __name__ == "__main__":
    lst = [6,5,4,3,2,1]
    quick(lst)
    print (lst)

