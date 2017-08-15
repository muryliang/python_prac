def shell(lst):
    """first choose the gap, then from start to gap-1, do insert over stride gap"""
    gaplist = list()
    tmpgap = 1
    while tmpgap < len(lst):
        gaplist.append(tmpgap)
        tmpgap = 3**tmpgap + 1 

    while len(gaplist) > 0:
        gap = gaplist.pop()
        for i in range(gap):
            insertsort(lst, i, gap)

def insertsort(lst, start, gap):
    for i in range(start + gap, len(lst), gap):
        idx = i
        tmp = lst[i]
        while idx - gap >= 0 and lst[idx-gap] > tmp:
            lst[idx] = lst[idx-gap]
            idx -= gap
        lst[idx] = tmp

        
if __name__ == "__main__":
    lst = [6,5,4,3,2,1]
    shell(lst)
    print (lst)

