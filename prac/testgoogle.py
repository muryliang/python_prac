import requests
from lxml.html import fromstring
import pickle
from requests.packages.urllib3.exceptions import MaxRetryError
import os

with open("/home/sora/proxy.dat", "rb") as f:
    proxylst = pickle.load(f)

headers = headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'}
ipurl = "http://ip.cn"

staticfile = "/home/sora/proxyfilte.dat"
testtimeout = 8

def store(obj, sfile):
    with open(sfile, "wb") as f:
        pickle.dump(obj, f)

def load(sfile):
    with open(sfile, "rb") as f:
        res = pickle.load(f)
    return res

if not os.path.exists(staticfile):
    in_nouse = set()
    in_canuse = set()
#    out_nouse = set()
#    out_canuse = set()
    staticdict = {}
else:
    staticdict = load(staticfile)
    in_canuse, in_nouse = staticdict['in_canuse'], staticdict['in_nouse']


try:
    for ip, port in proxylst:
        if (ip, port) in list(in_nouse) + list(in_canuse):
            print ("previously detected no use, skip", ip, port)
            continue
        try:
            print ("trying", ip, port)
            proxies = {'http':'http://' + ip + ':' + port, 'https':'https"//' + ip + ':' + port}
            page = requests.get(ipurl, headers = headers, proxies = proxies, timeout = testtimeout)
            print ("success ip", ip, port)
            tree = fromstring(page.text)
            yourip = tree.xpath("//div[@id='result']/div/p/code/text()")
            print ("your ip is ", yourip)
            in_canuse.add((ip, port))
        except Exception as e:
            print (ip, port ,"some failed, ignore")
            print (e)
            in_nouse.add((ip, port))
        #try google
        try:
            print ("trying", ip, port)
            proxies = {'http':'http://' + ip + ':' + port, 'https':'https"//' + ip + ':' + port}
            page = requests.get(ipurl, headers = headers, proxies = proxies, timeout = testtimeout)
            print ("success ip", ip, port)
            tree = fromstring(page.text)
            yourip = tree.xpath("//div[@id='result']/div/p/code/text()")
            print ("your ip is ", yourip)
            in_canuse.add((ip, port))
        except Exception as e:
            print (ip, port ,"some failed, ignore")
            print (e)
            in_nouse.add((ip, port))
finally:
    print ("in canuse", in_canuse, len(in_canuse))
    print ("in nouse", in_nouse, len(in_nouse))
    staticdict['in_nouse'] = in_nouse
    staticdict['in_canuse'] = in_canuse
    store(staticdict, staticfile)
    print ("stored done")
