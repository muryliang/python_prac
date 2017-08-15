import random
import quick
import quick2
import shell
import merge
import sys

"""use this to test sort performance"""

num = int(sys.argv[2])
sort = sys.argv[1]

lst = [random.randint(0, num-1) for _ in range(num)]
#lst = [20 for _ in range(num)]
#lst = [i  for i in range(num)]
#random.shuffle(lst)
if sort == "quick":
    quick.quick(lst)
elif sort == "quick2":
    quick2.quick(lst)
elif sort == "merge":
    merge.merge(lst)
elif sort == "shell":
    shell.shell(lst)
#print (lst)



