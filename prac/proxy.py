import requests
from lxml.html import fromstring
import pickle
import os

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36', 'Host':'www.gatherproxy.com'}
starturl = "http://www.gatherproxy.com/zh/"

if os.path.exists("/home/sora/proxy.dat"):
    with open("/home/sora/proxy.dat", "rb") as f:
        proxylst = pickle.load(f)
else:
    proxylst = set()

page = requests.get(starturl, headers= headers)
tree = fromstring(page.text)

lst = tree.xpath("//table//script[@type='text/javascript']/text()")
iplst = [ tmp.split(",")[2].split(":")[1].strip("\"") for tmp in lst]
portlst = [ str(int(tmp.split(",")[4].split(":")[1].strip("\""),base=16)) for tmp in lst]

for tmp in zip(iplst, portlst):
    proxylst.add(tmp)
print (proxylst, len(proxylst))

with open("/home/sora/proxy.dat", "wb") as f:
    pickle.dump(proxylst, f)
