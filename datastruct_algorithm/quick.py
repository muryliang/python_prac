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
    idx = midOfThree(lst, lo, hi)
    lst[lo], lst[idx] = lst[idx], lst[lo]

    sample = lst[lo]
    left = lo + 1
    right = hi
    done = False

    while not done:
        while left <= right and lst[left] <= sample:
            left += 1
        while right >= left and lst[right] >= sample:
            right -= 1

        if right < left:
            done = True
        else:
            lst[right], lst[left] = lst[left], lst[right]

    lst[lo], lst[right] = lst[right], lst[lo]
    return right

def qsort(lst, lo, hi):
    limit = 13
    if hi > lo:
        if hi - lo < limit:
            insert.insertInto(lst, lo, hi)
        splitpoint = split(lst, lo, hi)

        qsort(lst, lo, splitpoint-1)
        qsort(lst, splitpoint+1, hi)

if __name__ == "__main__":
    lst = [6,5,4,3,2,1]
    quick(lst)
    print (lst)

