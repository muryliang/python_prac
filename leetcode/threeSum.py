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
    

if __name__ == "__main__":
    lst = [-1, 0, 1, 2, -1, -4]
    print (threeSum(lst))
