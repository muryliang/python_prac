from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), "html.parser")
#url = bsObj.find("a", {"id":"logo"}).find("img")["src"]
url = bsObj.find("img")["src"]
print ("url", url)
#urlretrieve(url, "logo.jpg")
