import time

def perform(a, b, goal, failset, trueset):
    """a is limaL, b is limbL, failset is a list failseting action"""
#    time.sleep(1)
#    print(a, b)

    global lima
    global limb
    res = False
    if a == goal or b == goal:
        return True

    if res is False and a > 0 and b < limb and (a, b, "rmove") not in failset:
        failset.append((a, b, "rmove"))
        res = perform(max(a - (limb-b), 0), min(limb, b + a), goal, failset, trueset)
        if res:
            trueset.append("rmove")
    if res is False and b > 0 and a < lima and (a, b, "lmove") not in failset:
        failset.append((a, b, "lmove"))
        res = perform(min(lima, a + b), max(b - (lima-a), 0), goal, failset, trueset)
        if res:
            trueset.append("lmove")
    if res is False and b > 0 and (a, b, "drop b") not in failset:
        failset.append((a, b, "drop b"))
        res = perform(a, 0, goal, failset, trueset)
        if res:
            trueset.append("drop b")
    if res is False and a > 0 and (a, b, "drop a") not in failset:
        failset.append((a, b, "drop a"))
        res = perform(0, b, goal, failset, trueset)
        if res:
            trueset.append("drop a")
    if res is False and a < lima and (a, b, "fill a") not in failset:
        failset.append((a, b, "fill a"))
        res = perform(lima, b, goal, failset, trueset)
        if res:
            trueset.append("fill a")
    if res is False and b < limb and (a, b, "fill b") not in failset:
        failset.append((a, b, "fill b"))
        res = perform(a, limb, goal, failset, trueset)
        if res:
            trueset.append("fill b")
#    if res is False:
#        print ("nothing true, return")
    return res

failset = list()
trueset = list()
lima = 16
limb = 3
if perform(0, 0, 8, failset, trueset):
    print ("success")
else:
    print ("fail")
print (list(reversed(trueset)))
