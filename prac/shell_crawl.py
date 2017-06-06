from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring
import os
import dbhelper as db

start_url = 'http://site1.zjou.edu.cn/fish/shell_1.asp?px=id&lx=%CE%DE%B0%E5%B8%D9%2C+%B5%A5%B0%E5%B8%D9%2C+%B6%E0%B0%E5%B8%D9%2C+%B8%B9%D7%E3%B8%D9%2C+%BE%F2%D7%E3%B8%D9%2C+%CB%AB%BF%C7%B8%D9%2C+%CD%B7%D7%E3%B8%D9&PageNo=1&typer=0&key=&liker=1&page=40&order=ASC'

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US,en;q=0.5', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

host = "127.0.0.1"
user = "root"
passwd = "123456"
dbname = "fishdb"
table = "shelltable"

conn, cur = db.get_or_create_db(host = host, user = user, passwd = passwd, db = dbname)
db.create_twtable_if_needed(cur, table)

start_page = requests.get(start_url, headers = headers)
start_page.encoding = 'gbk'
#bsobj = BeautifulSoup(start_page.text, 'html.parser')
#bsobj.body
tree = fromstring(start_page.text)
nameurls = tree.xpath("//span[@class='style5']/a/@href")
basedir = "/mnt/sdb1/shell"

#clist = dict()
count = 0
for nameurl in nameurls:
        shellurl = urljoin(start_url, nameurl)
        page_response = requests.get(shellurl, headers = headers)
        page_response.encoding = 'gbk'
        bsobj = BeautifulSoup(page_response.text, 'html.parser')
        tbl = bsobj.body.findAll("table")[1].findAll("td")
        imgs = tbl[2:4]
        name = tbl[1].get_text().strip()
#        clist[name] = dict() 
#        for i in range(0, len(tbl), 2):
#            clist[name][tbl[i].get_text().strip()] = tbl[i+1].get_text().strip()
        for pic in imgs:
            info = dict()
            link = pic.find("img").attrs['src']
            join_link = urljoin(start_url, link)
            key_name = link.split('/')[-1]
            pic_content = requests.get(join_link).content
            #### store pictures in to file
            storedir = os.path.join(basedir, name)
            filename = os.path.join(storedir, key_name)
            if not os.path.exists(storedir):
                os.makedirs(storedir)
            with open(filename, "wb") as f:
                f.write(pic_content)
            info['Spidername'] = 'shellspider'
            info['fromUrl'] = shellurl
            info['imgurl'] = join_link
            info['imgsavename'] = filename.split('/')[-1]
            info['width'] = 250
            info['height'] = 250
            info['size'] = 250
            info['type'] = 'jpg'
            info['desc'] = ''
            info['name'] = name
            print ("get link", join_link)
            db.insert_info_one(conn, cur, table, info, basedir)
        print ("collected!!: ")
        count = count + 1
print ("all ", count , "items")
conn.commit()
cur.close()
conn.close()
