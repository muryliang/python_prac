import requests
import re
from string import ascii_lowercase
import threading
import pickle

starturl = 'http://www.algaebase.org/search/images/'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}

dictionary = dict()
lock = threading.Lock()
index = 0
lst = list(ascii_lowercase)

def calculate():
    post_params = {'-Search': 'Search', 'currentMethod': 'imgs', 'displayCount': '20', 'fromSearch': 'yes', 'query': ''}
    global total
    global dictionary
    args = get_next()
    while args != None:
        print ("start processing",args,"on", threading.currentThread().getName(),"letter", args)
        for j in ascii_lowercase:
            search_str = args + j
            post_params['query'] = search_str
            try:
                page = requests.post(starturl, data = post_params, headers = headers)
                count = int(re.match('.*<b>([0-9]+)</b> Found.*', str(page.content)).group(1))
            except AttributeError as e:
                print ("AttributeError, continue", search_str)
                continue
            if count > 3000:
                print ("need add sub for", search_str, count)
                add_new(search_str)
            else:
                dictionary[search_str] = count
                print (search_str, " count :", count)
        args = get_next()
    print ("thread", threading.currentThread().getName(),"done")

def add_new(arg):
    lock.acquire()
    lst.append(arg)
    lock.release()

def get_next():
    global index
    lock.acquire()
    if index >= len(lst):
        next_index = None
    else:
        next_index = lst[index] 
        index += 1
    lock.release()
    return next_index

thread_arr = []
for _ in range(8):
    t = threading.Thread(target=calculate)
    thread_arr.append(t)
    t.start()

try:
    for i in range(8):
        thread_arr[i].join()
finally:
    print (dictionary)
    #print ("total count is", total)
    with open("/tmp/calfile.dat", "wb") as f:
        pickle.dump(dictionary, f)
        print ("dump over")
