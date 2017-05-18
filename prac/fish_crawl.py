from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring
import re
import time
import string
import os
import pickle

clist = dict()
total_count = 0
storepath = "/home/sora/git/python/prac/setstore.dat"
if os.path.exists(storepath):
    with open(storepath, "rb") as f:
        cset = pickle.load(f)
else:
    cset = set()

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US,en;q=0.5', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

try:
    for pattern in string.ascii_lowercase:
        start_url = 'http://site1.zjou.edu.cn/fish/fish_1.asp?px=id&PageNo=1&typer=yw&key='+pattern+'&liker=0&page=5000&order=ASC'
        print ("start searching pattern", pattern)
        count = 0
        start_page = requests.get(start_url, headers = headers)
        start_page.encoding = 'gbk'
        tree = fromstring(start_page.text)
        nameurls = tree.xpath("//span[@class='style5']/a/@onclick")
        names = tree.xpath("//span[@class='style5']/a/text()")
        #学名这个有漏的，不能这样匹配，会移位，只能在里面找
        #scinames = tree.xpath("//span[@class='style5']/i/text()")
#        print (len(names), len(nameurls))
        for name, nameurl in zip(names, nameurls):
            if nameurl in cset:
                continue
            cset.add(nameurl)
            parturl = re.match("MM_openBrWindow\('(fish[^']*).*", nameurl).group(1) 
            wholeurl = urljoin(start_url, parturl)
            infopage = requests.get(wholeurl, headers = headers)
            # 网页的charset里是gb2312，但是实际使用发现gbk才能保证没有乱码字符,gb2312偶尔会乱码某些字符，如"鱚"不行
            infopage.encoding = 'gbk'
            infoobj = BeautifulSoup(infopage.text, 'html.parser')
            tbl = infoobj.body.table.findAll("tr")[1].td.findAll("tr") 
            imgs = tbl[5]
            tbl = tbl[:5]
            clist[name] = dict()
            print ("processing:", tbl[0].td.font.b.contents)
            clist[name]['中文名'] = name
            sciname = tree.xpath("//span[@class='style5']/i[../a/text()=\'"+name+"\']/text()")
            print ("sciname is", sciname)
            if len(sciname) == 0:
                clist[name]['学名'] = tbl[0].td.font.b.em.get_text()
            else :
                clist[name]['学名'] = sciname[0]
        # 不同物种里的结构不一样，有些不能用contents分，需要正则结合之前的学名来获取，价值不大，先不弄
        #    clist[name]['recorder'] = "".join([str(k).strip('</em>') for k in tbl[0].td.font.b.contents[2:]])

            for i in range(1,4):
                clist[name][tbl[i].findAll("td")[0].get_text().strip().replace('\xa0','')] = \
                    tbl[i].findAll("td")[1].get_text().strip().replace('\xa0','')
            print ("after processing:", clist[name])

            clist[name]['描述'] = tbl[4].findAll("td")[0].get_text().strip().replace('\xa0','')

            for imgsrc in imgs.findAll("img"):
                imgurl = urljoin(start_url, imgsrc['src'])
                postfix = imgurl.split('/')[-1]
                imgcontent = requests.get(imgurl, headers= headers)
                clist[name][postfix] = imgcontent.content
                filename = os.path.join("/tmp/pic", postfix)
                with open(filename, "wb+") as f:
                    f.write(imgcontent.content)
            print ("finish count", count, "pattern", pattern, "collected", name, clist[name].keys())
            count = count + 1
            total_count = total_count + 1
            time.sleep(0.1)
    print ("count is", count)
except Exception as e:
    print ("some error", e)
finally:
    with open(storepath, "wb")  as f:
        pickle.dump(cset, f)
    print ("total count is", total_count)
