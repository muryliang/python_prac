"""这个程序是用来计算给定的字符串的每种排列的"""
def mul(f):
    s = 1
    for i in range(2,f+1):
       s = s * i
    return s

def alllist(slist):
    if len(slist) == 1:
        yield slist
        # when only one element, yield return an iterator, 
        #but return just return a list, can not used in for ... in. ...
    else:
        char = slist[0]
        for order in alllist(slist[1:]):
            for i in range(len(order)+1):
        #        print (slist[:i] + [char] + slist[i:])
                yield order[:i] + [char] + order[i:]

string = input("input your string: ")
slist = list(string)
count = 0
print ("mul of %d is %d"%(len(slist), mul(len(slist))))
for i in alllist(slist):
#    print (i, end="  ")
    count += 1
#print ("\n")
print ("count is %d"%(count))
