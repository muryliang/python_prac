#!/usr/bin/python2
#filename:multi.py

from multiprocessing import Queue,Process,Pool
import time,random

def write(q):
    for value in [1,2,3]:
        print 'Put %s to queue...'%value
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue' %(value)

if __name__ == '__main__':
    q = Queue()
#    pw = Process(target = write, args=(q,))
#    pr = Process(target = read, args = (q,))
#    pw.start()
#    pr.start()
#    pw.join()
#    pr.terminate()
    p = Pool(6)
    for i in range(3):
        p.apply_async(write,args=(q,))
   #     p.apply_async(read, args=(q,))
    print 'Done'
    p.close()
    p.join()
