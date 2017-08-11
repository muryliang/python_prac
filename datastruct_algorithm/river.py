import time

def perform(x, y, boat, donelist, reslist):
    """ x, y are start side of river's member, x must >= y
        boat is either left or right
        donelist is context already seen
        reslist store final solution
    """

    global limx
    global limy
    if (x, y, boat) in donelist:
        print ("already do this")
        return False

    if x < 0 or y < 0 or x > limx or y > limy:
        print ("not exist")
        return False

    if (x != 0 and x < y) or (limx != x and limx - x < limy - y):
        print ("will eaten")
        return False

    if (x, y, boat) == (0, 0, "right"):
        return True

    ## always print left side remaining
    print ("do",x, y, boat)
    donelist.append((x, y, boat)) 

    # we will seperate two condition here, boat at left or right
    # in each condition, we should consider:
    #   from the boat side to another side: two people, two wolf, one people one wolf
    #                                        one people, one wolf
    res = False
    if boat == "left":
        dest = "right"
    else:
        dest = "left"

    if boat == "left":
        if res == False:
            print ("move two people from %s to %s"%(boat, dest))
            res = perform(x-2, y, dest, donelist, reslist)
            if res:
                reslist.append((x-2, y, dest))
        if res == False:
            print ("move each one from %s to %s"%(boat, dest))
            res = perform(x-1, y-1, dest, donelist, reslist)
            if res:
                reslist.append((x-1, y-1, dest))
        if res == False:
            print ("move two ghost from %s to %s"%(boat, dest))
            res = perform(x, y-2, dest, donelist, reslist)
            if res:
                reslist.append((x, y-2, dest))
        if res == False:
            print ("move one people from %s to %s"%(boat, dest))
            res = perform(x-1, y, dest, donelist, reslist)
            if res:
                reslist.append((x-1, y, dest))
        if res == False:
            print ("move one ghost from %s to %s"%(boat, dest))
            res = perform(x, y-1, dest, donelist, reslist)
            if res:
                reslist.append((x, y-1, dest))

    else:
        if res == False:
            print ("move two people from %s to %s"%(boat, dest))
            res = perform(x+2, y, dest, donelist, reslist)
            if res:
                reslist.append((x+2, y, dest))
        if res == False:
            print ("move each one from %s to %s"%(boat, dest))
            res = perform(x+1, y+1, dest, donelist, reslist)
            if res:
                reslist.append((x+1, y+1, dest))
        if res == False:
            print ("move two ghost from %s to %s"%(boat, dest))
            res = perform(x, y+2, dest, donelist, reslist)
            if res:
                reslist.append((x, y+2, dest))
        if res == False:
            print ("move one people from %s to %s"%(boat, dest))
            res = perform(x+1, y, dest, donelist, reslist)
            if res:
                reslist.append((x+1, y, dest))
        if res == False:
            print ("move one ghost from %s to %s"%(boat, dest))
            res = perform(x, y+1, dest, donelist, reslist)
            if res:
                reslist.append((x, y+1, dest))
    if not res:
        print ("faile in this")

    return res

donelist = list()
reslist = list()
limx = 3
limy = 3
if perform(limx, limy, 'left', donelist, reslist):
    print ("success")
else:
    print ("fail")

print (list(reversed(reslist)))
