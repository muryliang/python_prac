def twoSum(nums, target):
    """前提：只有一个解，列表无序，需要返回解对应的两个数字的原始下标
            这里的方法，加入hash，考虑重复的情况，hash加入一个tuple，包括
            对应数字以及一个下标，从1开始，所有重复的全部设为2,这里因为只有
            一个解，所以多于2个的可以不考虑。每次取一个元素后，删掉自己，然后
            在字典里找是否有剩余的可用解，有就返回，需要测试下标1,2两个情况的
    """
    dic = dict()
    for idx, elem in enumerate(nums):
        if (elem,1) not in dic:
            dic[(elem,1)] = idx
        else:
            dic[(elem,2)] = idx
    for elem, idx in list(dic.keys()):
        sub = target - elem
        val = dic[(elem,idx)]
        del dic[(elem,idx)]
        if (sub,1) in dic:
            return [min(val, dic[(sub,1)]), max(val,dic[(sub,1)])]
        elif (sub,2) in dic:
            return [min(val, dic[(sub,2)]), max(val,dic[(sub,2)])]
        dic[(elem,idx)] = val
    return []

def twoSum2(nums, target):
    """this method use sort with a tuple,
        a tuple sort will first sort the first number, then second,
        we can take advantage of this
    """
    lst = [(key, idx) for idx, key in enumerate(nums)]
    lst.sort()
    start = 0
    end = len(lst)-1
    while start < end:
        res = target - lst[start][0]
        if res > lst[end][0]:
            start += 1
        elif res < lst[end][0]:
            end -= 1
        else:
            one = lst[start][1]
            two = lst[end][1]
            return [min(one, two), max(one, two)]
    return []


if __name__ == "__main__":
    lst = [2,7,11,15]
    target = 9
    print (twoSum2(lst, target))


