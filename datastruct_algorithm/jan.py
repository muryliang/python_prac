import time
import sys

def perform(a, b, goal, failset, trueset):
    """a is limaL, b is limbL, failset is a list failseting action"""
#    time.sleep(1)
#    print(a, b)

    global lima
    global limb
    res = False
    if a == goal or b == goal or a + b == goal:
        return True

    if res is False and a > 0 and b < limb:
        ares = max(a - (limb-b), 0)
        bres = min(limb, b + a)
        if (ares , bres) not in failset:
            failset.append((ares, bres) )
            res = perform(ares, bres, goal, failset, trueset)
            if res:
                trueset.append("rmove")
    if res is False and b > 0 and a < lima:
        ares = min(lima, a + b)
        bres = max(b - (lima-a), 0)
        if (ares , bres) not in failset:
            failset.append((ares, bres))
            res = perform(ares, bres,  goal, failset, trueset)
            if res:
                trueset.append("lmove")
    if res is False and b > 0:
        ares = a
        bres = 0
        if (ares , bres) not in failset:
            failset.append((ares, bres))
            res = perform(ares, bres,  goal, failset, trueset)
            if res:
                trueset.append("drop b")
    if res is False and a > 0:
        ares = 0
        bres = b
        if (ares , bres) not in failset:
            failset.append((ares, bres))
            res = perform(ares, bres,  goal, failset, trueset)
            if res:
                trueset.append("drop a")
    if res is False and a < lima:
        ares = lima
        bres = b
        if (ares , bres) not in failset:
            failset.append((ares, bres))
            res = perform(ares, bres,  goal, failset, trueset)
            if res:
                trueset.append("fill a")
    if res is False and b < limb:
        ares = a
        bres = limb
        if (ares , bres) not in failset:
            failset.append((ares, bres))
            res = perform(ares, bres,  goal, failset, trueset)
            if res:
                trueset.append("fill b")
#    if res is False:
#        print ("nothing true, return")
    return res

failset = [(0,0)]
trueset = list()

lima = int(sys.argv[1])
limb = int(sys.argv[2])
goal = int(sys.argv[3])
if perform(0, 0, goal, failset, trueset):
    print ("success")
else:
    print ("fail")
print (list(reversed(trueset)))
