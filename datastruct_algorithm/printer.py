from random import randrange
import time
import math
from queue import Queue

class Printer():
    """this is a model of printer"""

    def __init__(self, pagePerMin):
        self.pagePerSec = pagePerMin / 60
        self.time = 0

    def addJob(self, job):
        """calculate time in sec from job's page"""
        self.time = math.ceil(job.pages / self.pagePerSec)

    def decTime(self):
        if self.time > 0:
            self.time -= 1

    def isFree(self):
        return self.time == 0

class Job():
    """this describe a job of pages"""

    def __init__(self, pages, time):
        self.pages = pages
        self.currentSecond = time

def simulate():
    """every second create a job in 1/180 rate, then add to queue"""

    q = Queue()
    p = Printer(10) # 10 pages per min
    count = 0
    totaltime = 0
    CEIL = 100
    while True:
        if randrange(0, 180) == 179:
            job = Job(randrange(0, 20) + 1, time.time())
            print ("create one job", job.currentSecond)
            q.enqueue(job)
            count += 1 # used for stop
            if p.isFree():
                deq = q.dequeue()
                totaltime += time.time() - deq.currentSecond
                p.addJob(deq)
                print ("add to printer %f, last for %d sec"%(deq.currentSecond, p.time))
        p.decTime() # reduce printer time
        if count == CEIL:
            break
        time.sleep(0.001) # 1 milisecond to simulate 1 second
    print ("done, all waiting time is %.3f and avg is %.6f"%(totaltime, totaltime / CEIL))

if __name__ == "__main__":
    simulate()
