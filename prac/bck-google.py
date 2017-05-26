import json
from bs4 import BeautifulSoup
from six.moves.urllib.parse import urlencode
import requests
import time
import pickle
from urllib.request import urlretrieve
import urllib
import socket
import os

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'}
base_url = 'https://www.google.com/search?'
ddir = "/tmp/gfish"
urllib.request.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'
#socket.setdefaulttimeout(5)

alldict = dict()

search_str = "Cololabis saira"
info = dict() # this for one species
info['name'] = search_str
index = 0
#info['chiname'] =  chinese

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

#test only can fetch less than 10 pages, so 12 is enough
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
        if download_img(info[index], os.path.join(ddir, search_str)):
            print ("finish page", info[index]['imgsavename'])
            index += 1
        else:
            print ("skip page", info[index]['imgsavename'])
            
alldict[search_str] = info

with open("/tmp/sets.dat", "wb") as f:
    pickle.dump(alldict, f)
