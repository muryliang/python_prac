def shell(lst):
    """first choose the gap, then from start to gap-1, do insert over stride gap"""

    gap = len(lst) // 2

    while gap >= 1:
        for i in range(gap):
            insertsort(lst, i, gap)
        gap //=2

def insertsort(lst, start, gap):
    for i in range(start + gap, len(lst), gap):
        idx = i
        tmp = lst[i]
        while idx - gap >= 0 and lst[idx-gap] > tmp:
            lst[idx] = lst[idx-gap]
            idx -= gap
        lst[idx] = tmp

        
lst = [6,5,4,3,2,1]
shell(lst)
print (lst)

