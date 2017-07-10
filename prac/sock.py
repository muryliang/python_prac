import requests
#import socks
import socket
import pickle

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'}

proxies = {
        'http':'http://{0}:{1}',
        'https':'http://{0}:{1}',
}

success = list()
#socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
#socket.socket = socks.socksocket
starturl = "https://www.facebook.com"
googleurl = "https://www.google.com"
ifconfigme = "http://ifconfig.me/ip"
imgurl = 'https://www.google.com/search?q=Cololabis+saira&ijn=0&start=0&tbm=isch'

mod = "http://{0}:{1}"
#with open("/home/sora/proxy.dat", "rb") as f:
#    lst = pickle.load(f)
try:
#    for ip,port in lst:
#A        print ("try ", ip, port)
#        try:
#            page = requests.get(ifconfigme, headers = headers, proxies={'http':mod.format(ip,port),'https':mod.format(ip,port)}, timeout=3)
        page = requests.get(ifconfigme, headers = headers, proxies={'http':mod.format('127.0.0.1','8118'),'https':mod.format('127.0.0.1','8118')}, timeout=3)
        print (page.text)
        print (ip, port, "success")
#            success.append((ip, port))
#        except Exception as e:
#            print ("cat not get")
#            print (e)
#        print ("")
finally:
    print (success)
#    with open("/home/sora/store.dat", "wb") as f:
#        pickle.dump(success, f)
