def twoSum(nums, target, pos):
    lst = nums
    start = pos
    end = len(nums)-1
    reslist = []
    while start < end:
        res = target - nums[start]
        if res > nums[end]:
            start += 1
        elif res < nums[end]:
            end -= 1
        else:
            reslist.append([nums[start], nums[end]])
            while end -1 > start and nums[end-1] == nums[end]:
                end -= 1
            end -= 1
            while start + 1 < end and nums[start+1] == nums[start]:
                start += 1
            start += 1
    return reslist

def threeSum(nums, target, pos):
    """find three numbers sum to 0, first select one ,then find another two's target"""
    reslist = list()
    for i in range(pos, len(nums)):
        if i == pos or nums[i] != nums[i-1]: #forbid duplicate
            sublist = twoSum(nums, target-nums[i], i+1)
            for lst in sublist:
                reslist.append([nums[i], lst[0], lst[1]])
    return reslist

def fourSum(nums, target):
    """find three numbers sum to 0, first select one ,then find another two's target"""
    nums.sort()
    reslist = list()
    for idx, elem in enumerate(nums):
        if idx == 0 or elem != nums[idx-1]: #forbid duplicate
            sublist = threeSum(nums, target-elem, idx+1)
            for lst in sublist:
                reslist.append([elem, lst[0], lst[1], lst[2]])
    return reslist
    

def fourSum2(nums, target):
#    nums.sort()
    """how to stip duplicate when create quad list ??, (3, (0,0)) (3,(0, 1)) ??"""
    quad = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                quad.append((nums[i]+nums[j], (nums[i], i), (nums[j], j)))
            else:
                quad.append((nums[i]+nums[j], (nums[j], j), (nums[i], i)))
    quad.sort()
    length = len(quad)
    i = 1
#    while i < length:
#        if quad[i][0] == quad[i-1][0]:
#            if quad[i][1][0] == quad[i-1][1][0] or quad[i][2][0] == quad[i-1][2][0]:
#                del quad[i]
#                length -= 1
#                continue
#        i += 1

    start = 0
    end = len(quad)-1
    reslist = []
    resset = set()
    while start < end:
        res = target - quad[start][0]
        if res > quad[end][0]:
            start += 1
        elif res < quad[end][0]:
            end -= 1
        else:
            groupstart = start
            groupend = end
            while start +1 < end and quad[start][0] == quad[start+1][0]:
                start += 1
            while end -1 > start and quad[end][0] == quad[end-1][0]:
                end -= 1
            addGroup(quad, groupstart, start, end, groupend, reslist, resset)
            start += 1
            end -= 1
    return reslist

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

if __name__ == "__main__":
    lst = [1, 0, -1, 0 ,-2, 2]
#    lst = [0,0,0,0]
#    lst = [-3,-1,0,2,4,5]
    target = 0
    print (fourSum2(lst, target))
