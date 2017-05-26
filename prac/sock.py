import requests
import socks
import socket

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'}

proxies = {
        'http':'socks5://127.0.0.1:1080',
        'https':'socks5://127.0.0.1:1080',
}


socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
socket.socket = socks.socksocket
starturl = "https://www.facebook.com"
googleurl = "https://www.google.com"
ifconfigme = "http://ifconfig.me/ip"
imgurl = 'https://www.google.com/search?q=Cololabis+saira&ijn=0&start=0&tbm=isch'
try:
    page = requests.get(imgurl, headers = headers)
    print (page.text)
except Exception as e:
    print ("some wrong")
    print (e)
