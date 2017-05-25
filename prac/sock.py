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
imgurl = 'https://www.google.com/search?site=imghp&tbm=isch&source=hp&biw=1280&bih=612&q=ko&oq=ko&gs_l=img.3...25947.29182.0.29483.13.13.0.0.0.0.306.608.3-2.2.0....0...1.1j4.64.img..11.2.604.0..0.eVmz_WCcEGQ'
try:
    page = requests.get(starturl, headers = headers)
    print (page.text)
except Exception as e:
    print ("some wrong")
    print (e)
