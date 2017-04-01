import random
def conflict(state, pos):
    """
    state: before current line, we have make sure all have non-conflict,and this is a tuple of that place
    pos: we put current on that pos ,return boolean whether will conflict
    """
    num = len(state)
    for i in range(num):
        if abs(state[i] - pos) in (0, num - i):
            return True
    return False

def queen(num = 8, state = ()):
    """
    check if conflict, if not : 
        check if is last:
            if so, yield the last one
            if not, for every recursive call's return tuple,
                append current not conflict pos and add that tuple and return
    """
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queen(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(result):
    def printline(pos):
        print '*'*pos + 'X' + '*' * (len(result) - 1 - pos)
    for pos in result:
        printline(pos)
prettyprint(random.choice(list(queen(8))))
