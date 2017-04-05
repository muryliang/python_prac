from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from chardet import detect
import sys
string = 'http://pythonscraping.com/pages/page1.html'
string2 = 'http://www.pythonscraping.com/pages/warandpeace.html'

def getinfo(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print ("error:", e)
        return None
    try:
        spobj = BeautifulSoup(html.read(),'html.parser')
        print (type(spobj.findAll('head')))
        print (type(spobj.findAll('head')[0]))
        print (spobj.findAll('head'))
        return spobj.head.title
    except AttributeError as e:
        print ("error when attr ref:", e)
        return None

    
title = getinfo(string)
if title == None:
    print ("Title attr not found")
else:
    print (title)

