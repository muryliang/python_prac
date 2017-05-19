import threading
import string
import pickle

lst = list(string.ascii_lowercase)
for i in  range(0,26,4):
    print (lst[i:min(26,i+4)])

with open("/home/sora/git/python/prac/tmpdump", "wb") as f:
    pickle.dump(lst, f)
    
