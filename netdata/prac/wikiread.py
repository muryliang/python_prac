from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

pages = set()
random.seed(datetime.datetime.now())
def getlinks(articleUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
#    bsObj.find("div", {"id": "bodyContent"}).findAll("a",
#                href=re.compile("^(/wiki/)((?!:).)*$"))
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print (newPage)
                pages.add(newPage)
                getlinks(newPage)

getlinks("")
#links = getlinks("/wiki/Kevin_Bacon")
#while len(links) > 0:
#    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
#    print(newArticle)
#    links=getlinks(newArticle)
