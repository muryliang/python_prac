def merge(lst):
    """divide into two and sort and merge"""

    domerge(lst, 0, len(lst)-1)

def domerge(lst, lo, hi):
    """ all subscript are inclusive"""
    if hi <= lo:
        return lst

    mid = (lo + hi) // 2
    domerge(lst, lo, mid)
    domerge(lst, mid+1, hi)
    tmplst = lst[:]
    
    i, k, j = lo, lo, mid + 1
    while i <= mid and j <= hi:
        if tmplst[i] <= tmplst[j]:
            lst[k] = tmplst[i]
            i += 1
        else:
            lst[k] = tmplst[j]
            j += 1
        k += 1
    # handle remain in eigher
    while i <= mid:
        lst[k] = tmplst[i]
        k += 1
        i += 1
    while j <= hi:
        lst[k] = tmplst[j]
        k += 1
        j += 1


lst = [5,4,3,12,2,1]
merge(lst)
print (lst)
