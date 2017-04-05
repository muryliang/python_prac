from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError
import sys
import os
import re

url = "http://en.wikipedia.org/wiki/Kevin_Bacon"

#urlretrieve(url, "sample.html")
with open("sample.html") as f:
    bsobj = BeautifulSoup(f.read(), 'html.parser')

for link in bsobj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print (link.attrs['href'])
    
