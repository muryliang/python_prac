def quick(lst):
    qsort(lst, 0, len(lst)-1)

def split(lst, lo, hi):
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
    if hi > lo:
        splitpoint = split(lst, lo, hi)
        print ("after %d lst is"%(splitpoint), lst)

        qsort(lst, lo, splitpoint-1)
        qsort(lst, splitpoint+1, hi)

lst = [6,5,4,3,2,1]
quick(lst)
print (lst)

