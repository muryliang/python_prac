from queue import Queue
import time

def hotPotato(total, step):
    """ josephu ring

    total is number of all
    we kill one after pass every step steps"""

    q = Queue()
    for i in range(total):
        q.enqueue(i)
    prev = time.time()
    while q.size() > 1:
        for i in range(step):
            tmp = q.dequeue()
            q.enqueue(tmp)
        q.dequeue()
#        print ("killed ",q.dequeue())

    now = time.time()
    print ("the remaining one is", q.dequeue(), now - prev)

def fastPotato(total, step):
    """a fast implement of hotPotato

    in this method , step should plus one,
    because we here should show that after 
    we make step steps, we delete the current
    index's num
    the algorithm is:
        we first know at last the remaining is 0,
        then reverse that, k(n) = (k(n-1) + step(here is step + 1)) % n
        complexity is O(n)"""
    prev = time.time()
    res = 0
    for i in range(2, total+1):
        res = (res + step + 1) % i
    now = time.time()
    print ("the remaining one is", res, now - prev)

total, step = input("input total and step: ").split(" ")
#hotPotato(int(total), int(step))
fastPotato(int(total), int(step))
