def fourSumCount(A, B, C, D):
    """sort all two list, from one start, other end, add ,if not target ,just
    modify start or end, else change both and add count, careful duplicate count"""
    quad1 = []
    quad2 = []
    length = len(A)
    for i in range(length):
        for j in range(length):
            quad1.append(A[i]+B[j])
            quad2.append(C[i]+D[j])
    quad1.sort()
    quad2.sort()

    start = 0
    end = length**2-1
    count = 0
    length = length **2
    while start < length and end >= 0:
        if -quad1[start] > quad2[end]:
            start += 1
        elif -quad1[start] < quad2[end]:
            end -= 1
        else:
            groupstart = start
            groupend = end
            while start < length-1 and quad1[start+1] == quad1[start]:
                start += 1
            while end > 0 and quad2[end] == quad2[end-1]:
                end -= 1
            count += (start - groupstart+1) * (groupend - end + 1)
            start += 1
            end -= 1
    return count

def addGroup(quad, start ,starte, end, ende, reslist, resset):
    """ current question, how can we make sure no duplicate without set?"""
    for a in range(start, starte+1):
        for b in range(end, ende+1):
            if not quad[a][1] in (quad[b][1] ,quad[b][2]) and not quad[a][2] in (quad[b][1] ,quad[b][2]):
                # we should sort nums first to make sure here's sequence
                if quad[a][1][0] < quad[b][1][0]:
                    min1 = quad[a][1][0]
                    mid1 = quad[b][1][0]
                else:
                    mid1 = quad[a][1][0]
                    min1 = quad[b][1][0]
                if quad[a][2][0] < quad[b][2][0]:
                    max1 = quad[b][2][0]
                    mid2 = quad[a][2][0]
                else:
                    max1 = quad[a][2][0]
                    mid2 = quad[b][2][0]
                if mid1 <= mid2 and (min1, mid1, mid2, max1) not in resset:
                    reslist.append((min1, mid1, mid2, max1))
                    resset.add((min1, mid1, mid2, max1))
                elif mid1 > mid2 and (min1, mid2, mid1, max1) not in resset:
                    reslist.append((min1, mid2, mid1, max1))
                    resset.add((min1, mid2, mid1, max1))

def fourSumCount2(A, B, C, D):
    """use hash , store value as duplicate ones"""
    quad1 = []
    quad2 = dict()
    length = len(A)
    count = 0 
    for i in range(length):
        for j in range(length):
            quad1.append(A[i]+B[j])
            num = quad2.get(C[i]+D[j], 0)
            quad2[(C[i]+D[j])] = num + 1 
    for sum1 in quad1:
        count += quad2.get(-sum1, 0)

    return count


if __name__ == "__main__":
    A = [1,2]
    B = [-2,-1]
    C = [-1, 2]
    D = [0,2]
    print (fourSumCount2(A, B, C, D))
