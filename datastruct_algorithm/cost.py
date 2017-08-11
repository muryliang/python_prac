def convert(a, b):
    """this function find the least cost from convert a to b

    score, insert one letter, 20cost, 
    delete one: 20 cost
    copy one: 5 cost

    we use recursive method, every time compute one, record
    the least cost and the method in a dictionary for reuse
    """

    global dic
    if dic.get((a,b), (0,0)) != (0,0):
        return dic[(a,b)][0]
    cost = 1000
    index = -1
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            index = i
            break
    
    if index == -1:
        cost = max(len(a), len(b)) - min(len(a), len(b))
        cost *= 20
        res = "insert or remove"
#        print ("just remove or insert")
    else:
        res = "None"
        curcost = 5 + convert(a[index+1:], b[index+1:])
        if curcost < cost:
            cost = curcost
            res = "copy"
        curcost = 20 + convert(a[index:], b[index+1:])
        if curcost < cost:
            cost = curcost
            res = "insert"
        curcost = 20 + convert(a[index+1:], b[index:])
        if curcost < cost:
            cost = curcost
            res = "cost"
    dic[(a,b)] = (cost, res)
    return cost

dic = dict()
a = 'algorithm'
b = 'algoritttm'
print (convert(a,b))
print (dic)
