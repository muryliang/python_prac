import json
from bs4 import BeautifulSoup
from six.moves.urllib.parse import urlencode
import requests
import time
import pickle
import os
import threading

def download_img(inf, ddir):
    global headers
    if not os.path.exists(ddir):
        os.makedirs(ddir)
    filepath = os.path.join(ddir, inf['imgsavename'])
    try:
        content = requests.get(inf['imgurl'], headers = headers, timeout = 5)
    except Exception as e:
        print ("download failed , just return", inf['imgsavename'])
        return False
    with open(filepath, "wb") as f:
        f.write(content.content)
    print ("download pic done", inf['imgsavename'])
    return True

def lock_inc(obj):
    global lock
    lock.acquire()
    obj += 1
    lock.release()

def get_next():
    global lock
    global engname
    lock.acquire()
    if len(engname) != 0:
        next_item = engname.pop()
    else:
        next_item = None
    lock.release()
    return next_item

def calculate():
    global ddir
    search_str = get_next()
    curthread = threading.currentThread().getName()
    while search_str is not None:
        if search_str.replace(" ", "_") in exist_set:
            print (curthread,"already downloaded", search_str)
            continue
        print (curthread, "begin fetching", search_str)
        info = dict() # this for one species
        index = 0
        #test shows that  only can fetch less than 10 pages, otherwise return no content, so 12 is enough
        for i in range(0,12):
            print ("start loop", i)
            time.sleep(1)

        #    tbs = 'isz:l' #only big size img, but too little
            params = dict (q=search_str, ijn=i , start=i*100, tbm='isch')
            url = base_url + urlencode(params)
            page = requests.get(url, headers = headers)
            soup = BeautifulSoup(page.text, 'lxml')
            image_divs = soup.find_all('div', class_='rg_meta')
            # handle 100 imgs
            for div in image_divs:
                meta = json.loads(div.text)
                #set image's name
                info[index] = dict()
                info[index]['imgsavename'] = str(index) + ".jpg"
                info[index]['desc'] = meta.get('pt', None)
                info[index]['fromUrl'] = meta.get('ru', None)
                info[index]['name'] = search_str
                if 'ou' in meta:
                    info[index]['imgurl'] = meta['ou']
                    info[index]['height'] = meta['oh']
                    info[index]['width'] = meta['ow']
                elif 'tu' in meta:
                    info[index]['imgurl'] = meta['tu']
                    info[index]['height'] = meta['th']
                    info[index]['width'] = meta['tw']
                else:
                    info[index]['imgurl'] = None
                    info[index]['height'] = None
                    info[index]['width'] = None
                print ("got image:", info[index]['imgurl'])
                if download_img(info[index], os.path.join(ddir, search_str.replace(" ", "_"))):
                    print ("finish page", info[index]['imgsavename'])
                    index += 1
                else:
                    print ("skip page", info[index]['imgsavename'])
        alldict[search_str] = info
        exist_set.add(search_str.replace(" ", "_"))
        search_str = get_next()
    print (curthread,"thread done")
    lock_inc(done)

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'}
base_url = 'https://www.google.com/search?'
ddir = "/tmp/gfish"
#global dictionary, used to be stored and read
alldict = dict()

#get input from csv file
csvfile = "/home/jztec/fish/fishsorts.dat"
with open(csvfile, "rb") as f:
    fishnames = pickle.load(f)
engname = fishnames['engname'][:]

#search_str = "Cololabis saira"

#about thread manage
done = 0
lock = threading.Lock()
thread_arr = []
threads = 3
for _ in range(threads):
    t = threading.Thread(target=calculate)
    thread_arr.append(t)
    t.start()

try:
    while done < threads:
        time.sleep(10)
    print ("all threads done")
finally:
    with open("/tmp/fishgoogle.dat", "wb") as f:
        pickle.dump(alldict, f)
