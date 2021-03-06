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

def threeSum(nums):
    """find three numbers sum to 0, first select one ,then find another two's target"""
    nums.sort()
    reslist = list()
    for idx, elem in enumerate(nums):
        if idx == 0 or elem != nums[idx-1]: #forbid duplicate
            sublist = twoSum(nums, 0-elem, idx+1)
            for lst in sublist:
                reslist.append([elem, lst[0], lst[1]])
    return reslist

def threeSum2(nums):
    nums.sort()
    stopm = 0
    stopz = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            stopm += 1 
        elif nums[i] == 0:
            stopz += 1
    nump = nums[:stopm]
    numq = nums[stopm:]
    print (nump, numq)
    reslist = []
    if stopz >= 3:
        reslist.append([0,0,0])
    for i in range(0, len(numq)):
        if i == 0 or numq[i] != numq[i-1]:
            sublist = twoSum(nump, 0-numq[i], 0)
            for lst in sublist:
                reslist.append([lst[0], lst[1], numq[i]]) 
    for i in range(0, len(nump)):
        if i == 0 or nump[i] != nump[i-1]:
            sublist = twoSum(numq, 0-nump[i], 0)
            for lst in sublist:
                reslist.append([nump[i], lst[0], lst[1]])
    return reslist
    

if __name__ == "__main__":
    lst = [-1, 0, 1, 2, -1, -4]
    print (threeSum2(lst))
