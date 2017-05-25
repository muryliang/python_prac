import requests
import pickle
from urllib.request import urlretrieve
import urllib
import socket

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}
with open("/tmp/sets.dat", "rb") as f:
    kset = pickle.load(f)

socket.setdefaulttimeout(5)
uset = set()
for i in kset.keys():
    for j in kset[i]:
        uset.add(j)

urllib.request.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'
index = 0
for url in uset:
    try:
        print ("url", url)
        urlretrieve(url, "/tmp/bb/" + str(index) + ".jpg")
        print ("done")
    except:
        print ("just ignore")
    index += 1

