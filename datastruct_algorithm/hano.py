import time
import sys

def move(num, start, end, mid):
    """move from start to end, use mid to tmp store"""

    global count
    if num == 0:
        return
    move(num-1, start, mid, end)
    do_move(start, end)
    count += 1
    move(num-1, mid, end, start)

def do_move(start, end):
#    print ("move from %d to %d"%(start, end))
    pass

count = 0
numbers = int(sys.argv[1])
#numbers = int(input("input your panels: "))
tick = time.time()
move(numbers, 1, 3, 2)
print ("all cost %d steps, time %f"%(count, time.time() - tick))

