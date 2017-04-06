from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError
import sys, os, re, random, time

url = "http://en.wikipedia.org"

#urlretrieve(url, "sample.html")
def getlink(postfix):
    with urlopen(url + postfix) as f:
        bsobj = BeautifulSoup(f.read(), 'html.parser')

    links = bsobj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))
    link = (random.choice(links))['href']
    print ("href is", link)
    return link
    
saved = []
reslink = getlink("/wiki/Kevin_Bacon")
while True:
    try:
        if reslink == None:
            break
        reslink = getlink(reslink)
    except HTTPError as e:
        print ("httperror", e)
        sys.exit(1)
    except AttributeError as e:
        print ("attr error", e)
        sys.exit(1)

    if reslink in saved:
        print ("loop!!")
        break
    saved.append(reslink)
    time.sleep(3)

print (saved)

    


