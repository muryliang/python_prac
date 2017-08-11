import time

num = int(input("num: "))
def rec(num):
    if num <= 2:
        return num
    return rec(num-1) + rec(num-2)

def nrec(num):
    one = 1
    two = 2
    count = 0
    while count != num:
        three = one + two
        one = two
        two = three
        count += 1
    return three

cur = time.time()
#print (rec(num), time.time() - cur)
print (nrec(num), time.time() - cur)
