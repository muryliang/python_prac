import sys

def twoSumClosest(nums, target, elem, pos):
    start = pos
    end = len(nums)-1
    least = sys.maxsize
    res = sys.maxsize
    while start < end:
        diff = elem + nums[start] + nums[end]
        if diff - target < 0:
            if target - diff < res:
                least = diff
                res = target - diff
            start += 1
        elif diff - target > 0:
            if diff - target < res:
                least = diff
                res = diff - target
            end -= 1
        else:
            return diff

    return least

def threeSumClosest(nums, target):
    """method: like three, first find twoSumClosest, but return two list for 
        every element, one positive least pair, one negative pair
        the outer loop update the least pair every time
    """
    nums.sort()
    least = sys.maxsize # a very big number
    for idx, elem in enumerate(nums):
        tmpresult = twoSumClosest(nums, target, elem, idx+1)
        if abs(least - target) > abs(tmpresult - target):
            least = tmpresult
    return least

    

if __name__ == "__main__":
    lst = [0,1,2]
    target = 3
    print (threeSumClosest(lst, target))
