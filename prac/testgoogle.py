import requests
from lxml.html import fromstring
import pickle
from requests.packages.urllib3.exceptions import MaxRetryError
import os

with open("/home/sora/proxy.dat", "rb") as f:
    proxylst = pickle.load(f)

headers = headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'}
ipurl = "http://ip.cn"
googleurl = "http://www.google.com"

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
    out_nouse = set()
    out_canuse = set()
    staticdict = dict()
else:
    staticdict = load(staticfile)
    in_canuse, in_nouse, out_canuse, out_nouse = staticdict['in_canuse'], staticdict['in_nouse'], \
                staticdict.get('out_canuse', set()), staticdict.get('out_nouse', set())


try:
    for ip, port in proxylst:
        if (ip, port)  in list(in_nouse) + list(in_canuse):
            print ("previously detected no use or can use, skip", ip, port)
        else:
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
                print (ip, port ,"local failed, ignore")
                in_nouse.add((ip, port))
        #try google
        if (ip, port)  in list(out_nouse) + list(out_canuse):
            print ("previously detected no use or can use google, skip", ip, port)
        else:
            try:
                print ("trying google", ip, port)
                proxies = {'http':'http://' + ip + ':' + port, 'https':'https"//' + ip + ':' + port}
                page = requests.get(googleurl, headers = headers, proxies = proxies, timeout = testtimeout)
                print ("success google ip", ip, port)
                tree = fromstring(page.text)
                yourip = tree.xpath("//div[@id='result']/div/p/code/text()")
                print ("your ip is ", yourip)
                out_canuse.add((ip, port))
            except Exception as e:
                print (ip, port ,"goole failed, ignore")
                out_nouse.add((ip, port))
finally:
    print ("in canuse", in_canuse, len(in_canuse))
    print ("in nouse", in_nouse, len(in_nouse))
    print ("out canuse", in_canuse, len(in_canuse))
    print ("out nouse", in_nouse, len(in_nouse))
    staticdict['in_nouse'] = in_nouse
    staticdict['in_canuse'] = in_canuse
    staticdict['out_nouse'] = out_nouse
    staticdict['out_canuse'] = out_canuse
    store(staticdict, staticfile)
    print ("stored done")
