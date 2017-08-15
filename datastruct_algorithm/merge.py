import insert

def merge(lst):
    """divide into two and sort and merge"""

    flst = lst[:]
    domerge(lst, flst, 0, len(lst)-1)

def domerge(lst, flst, lo, hi):
    """ all subscript are inclusive
    
    from flst merge to lst"""
    limit = 13
    if hi <= lo:
        return
    if hi - lo < limit:
        insert.insertInto(lst, lo, hi)
        return

    mid = (lo + hi) // 2
    domerge(flst, lst, lo, mid)
    domerge(flst, lst, mid+1, hi)
    
    i, k, j = lo, lo, mid + 1
    while i <= mid and j <= hi:
        if flst[i] <= flst[j]:
            lst[k] = flst[i]
            i += 1
        else:
            lst[k] = flst[j]
            j += 1
        k += 1
    # handle remain in eigher
    while i <= mid:
        lst[k] = flst[i]
        k += 1
        i += 1
    while j <= hi:
        lst[k] = flst[j]
        k += 1
        j += 1


if __name__ == "__main__":
    lst = [5,4,3,12,2,1]
    merge(lst)
    print (lst)
