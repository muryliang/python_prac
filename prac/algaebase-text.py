import requests
import re
from string import ascii_lowercase
import threading
import pickle

starturl = 'http://www.algaebase.org/search/images/'
#headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.5', 'Connection': 'keep-alive', 'Content-Length': '72', 'Content-Type': 'application/x-www-form-urlencoded', 'DNT': '1', 'Host': 'www.algaebase.org', 'Referer': 'http://www.algaebase.org/search/images/', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}

dictionary = dict()
lock = threading.Lock()
index = 0

def calculate():
    post_params = {'-Search': 'Search', 'currentMethod': 'imgs', 'displayCount': '20', 'fromSearch': 'yes', 'query': ''}
    global total
    global dictionary
    args = get_next()
    while args is not None:
        print ("start processing",args,"on", threading.currentThread().getName(),"letter", ascii_lowercase[args])
        for j in ascii_lowercase:
            search_str = ascii_lowercase[args] + j
            post_params['query'] = search_str
            try:
                page = requests.post(starturl, data = post_params, headers = headers)
                count = int(re.match('.*<b>([0-9]+)</b> Found.*', str(page.content)).group(1))
            except AttributeError as e:
                print ("AttributeError, continue", search_str)
                continue
            dictionary[search_str] = count
            print (search_str, " count :", count)
        args = get_next()
    print ("thread", threading.currentThread().getName(),"done")

def get_next():
    global index
    lock.acquire()
    next_index = index 
    index += 1
    lock.release()
    if next_index > 25:
        return None
    return next_index

thread_arr = []
for _ in range(8):
    t = threading.Thread(target=calculate)
    thread_arr.append(t)
    t.start()

for i in range(8):
    thread_arr[i].join()

print (dictionary)
#print ("total count is", total)
with open("/tmp/calfile.dat", "wb") as f:
    pickle.dump(dictionary, f)
    print ("dump over")
