from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print (image.attrs["src"])
#for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
#    print (sibling)
#print (bsObj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
