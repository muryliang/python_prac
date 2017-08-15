def sel(lst):
    """ from start, every time select the max of current i numbers, change that with the ith number"""
    n = len(lst)
    for i in range(n-1, 1, -1):
        # we will start second range for whole number, so range(n) means 0~n-1, range(2) == 0~1 the last loop
        maxidx = 0
        for j in range(1, i+1):
            if lst[j] > lst[maxidx]:
                maxidx = j
        if maxidx != i:
            lst[maxidx], lst[i] = lst[i], lst[maxidx]

lst = [5,4,3,2,1]
sel(lst)
print (lst)
