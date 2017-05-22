import requests
import re
from string import ascii_lowercase
import threading
import pickle
from urllib.parse import urljoin
from lxml.html import fromstring
import os

starturl = 'http://www.algaebase.org/search/images/'

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}

dictionary = dict() # currently do not store any thing
lock = threading.Lock()
index = 0
lst = ['Ascophyllum nodosum', 'Fucus spiralis']

datafile = "/tmp/datafile.dat"
if os.path.exists(datafile):
    with open(datafile, "rb") as f:
        exist_set = pickle.load(f) # exist set
else:
    exist_set = set()

def calculate():
    post_params = {'-Search': 'Search', 'currentMethod': 'imgs', 'displayCount': '20', 'fromSearch': 'yes', 'query': ''}
    global total
    global dictionary
    args = get_next()
    while args is not None:
        print ("start processing",args,"on", threading.currentThread().getName(),"letter", args)
        search_str = args
        post_params['query'] = search_str
        try:
            page = requests.post(starturl, data = post_params, headers = headers)
            count = int(re.match('.*<b>([0-9]+)</b> Found.*', str(page.content)).group(1))
        except AttributeError as e:
            print ("AttributeError, continue", search_str)
            continue
        print (search_str, " count :", count)
        infodict = get_info(page)
        if infodict is not None:
            print ("get info of %s"%(infodict['name']), infodict)
            infodict['count'] = count
            dictionary[infodict['name']] = infodict
        else :
            print (search_str, "already exist")
        args = get_next()
    print ("thread", threading.currentThread().getName(),"done")

def get_next():
    global index
    lock.acquire()
    if len(lst) != 0:
        next_item = lst.pop()
    else:
        next_item = None
    lock.release()
    return next_item

def get_info(page):
    infodict = dict()
    tree = fromstring(page.text)
    #just search the first, most proper one
    bigimg, detailurl = tree.xpath("//tr/td/p/a/img/@src")[0], tree.xpath("//tr/td/p/a/@href[../img]")[0] 
    detailpage = requests.get(urljoin(starturl, detailurl), headers = headers)

    detailtree = fromstring(detailpage.text)
    infodict['name'] = " ".join(detailtree.xpath("//h2//i/text()"))
    if infodict['name'] in exist_set: #already exists
        return None
    else:
        exist_set.add(infodict['name'])
    otherurls = detailtree.xpath("//div[@id='random-img-grid']/a/div/@style") # a list
    infodict['imglist'] = [re.match(".*\(([^)]*)", tmp).group(1) for tmp in otherurls]
    infodict['imglist'].append(bigimg)
    return infodict

thread_arr = []
for _ in range(2):
    t = threading.Thread(target=calculate)
    thread_arr.append(t)
    t.start()

for i in range(2):
    thread_arr[i].join()

print (dictionary)
with open(datafile, "wb") as f:
    pickle.dump(exist_set, f)
    print ("dump over")
