import time

def perform(a, b, record, string):
    """a is 4L, b is 3L, record is a list recording action"""
    time.sleep(1)
    print (string, a, b)
    res = False
    if a == 2 or b == 2:
        return True

    if res is False and a > 0 and b < 3:
        res = perform(max(a - (3-b), 0), min(3, b + a), record, "move a to b")
        if res:
            record.append("move a to b")
    if res is False and b > 0 and a < 4:
        res = perform(min(4, a + b), max(b - (4-a), 0), record, "move b to a")
        if res:
            record.append("move b to a")
    if res is False and b > 0:
        res = perform(a, 0, record, "drop b")
        if res:
            record.append("drop b")
    if res is False and a > 0:
        res = perform(0, b, record, "drop a")
        if res:
            record.append("drop a")
    if res is False and a < 4:
        res = perform(4, b, record, "fill a")
        if res:
            record.append("fill a")
    if res is False and b < 3:
        res = perform(a, 3, record, "fill b")
        if res:
            record.append("fill b")
    if res is False:
        print ("nothing true, return")
    return res

lst = list()
perform(0, 0, lst, "null")
print (lst)
