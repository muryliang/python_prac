import pprint
import sys

def pascal(num, dic):
    """layer number start from 0"""

    if num == 0:
        dic[0].append(1)
    else:
        dic[num].append(1)
        for i in range(1, num):
            dic[num].append( dic[num-1][i-1] + dic[num-1][i])
        dic[num].append(1)

dic = list()
num = int(sys.argv[1])
for i in range(num):
    dic.append(list())
    pascal(i, dic)

pprint.pprint (dic)
