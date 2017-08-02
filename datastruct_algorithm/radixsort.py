import queue

mq = [2,348, 234, 984, 43,45,26,77,999,180]
lq = []
for _ in range(10):
    lq.append(queue.Queue())

def iterIndex(mq, lq, num):
    assert num > 0
    for decimal in mq:
        lq[decimal%(10**num)//(10**(num-1))].enqueue(decimal)
    mq.clear()
    for q in lq:
        while not q.isEmpty():
            mq.append(q.dequeue())
        q.clean()

print (mq)
iterIndex(mq, lq, 1)
iterIndex(mq, lq, 2)
iterIndex(mq, lq, 3)
print (mq)
