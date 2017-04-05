from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

string = "http://www.pythonscraping.com/pages/page3.html"
html = urlopen(string)
bsobj = BeautifulSoup(html.read(), 'html.parser')

result = bsobj.findAll(lambda tag: len(tag.attrs) == 2)
for res in result:
    print (dir(res))
    print ("over\n\n")
#images = bsobj.findAll('img', {'src':re.compile('\.\./img/gifts/img.*\.jpg')})
#for image in images:
#    print (image['src'])
#    print (image.attrs['src'])
        

