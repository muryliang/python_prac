from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring
import re
import time
import string
import os
import pickle
import dbhelper as db
from requests.packages.urllib3.exceptions import ConnectTimeoutError

total_count = 0
basedir = "/mnt/sdb1/fishsea"

host = "127.0.0.1"
user = "root"
passwd = "123456"
dbname = "fishdb"
table = "fishtable"

conn, cur = db.get_or_create_db(host = host, user = user, passwd = passwd, db = dbname)
db.create_twtable_if_needed(cur, table)

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US,en;q=0.5', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

nset = db.load_all(cur, "keyword", table)
print ("nset is ", nset)
try:
    for pattern in string.ascii_lowercase:
        start_url = 'http://site1.zjou.edu.cn/fish/fish_1.asp?px=id&PageNo=1&typer=yw&key='+pattern+'&liker=0&page=5000&order=ASC'
        print ("start searching pattern", pattern)
        count = 0
        time.sleep(3)
        try:
            start_page = requests.get(start_url, headers = headers, timeout=100)
        except Exception as e:
            print ("can not fetch pattern %s, continue"%(pattern))
            continue
        start_page.encoding = 'gbk'
        tree = fromstring(start_page.text)
        nameurls = tree.xpath("//span[@class='style5']/a/@onclick")
        names = tree.xpath("//span[@class='style5']/a/text()")
#        print (len(names), len(nameurls))
        for name, nameurl in zip(names, nameurls):
            if name in nset:
                print ("%s already downloaded, skip"%(name,))
                continue
            parturl = re.match("MM_openBrWindow\('(fish[^']*).*", nameurl).group(1) 
            wholeurl = urljoin(start_url, parturl)
            retry = 3
            while retry > 0:
                try:
                    infopage = requests.get(wholeurl, headers = headers, timeout = 5)
                    break
                except ConnectTimeoutError as e:
                    retry -= 1
                    print (name, "retry", retry)
                    time.sleep(3)
                except Exception as e:
                    retry = 0
                    print ("just continue")
            else:
                print ("get info connect error, just continue")
                continue

            # 网页的charset里是gb2312，但是实际使用发现gbk才能保证没有乱码字符,gb2312偶尔会乱码某些字符，如"鱚"不行
            infopage.encoding = 'gbk'
            infoobj = BeautifulSoup(infopage.text, 'html.parser')
            tbl = infoobj.body.table.findAll("tr")[1].td.findAll("tr") 
            imgs = tbl[5]
            tbl = tbl[:5]

            for imgsrc in imgs.findAll("img"):
                imgurl = urljoin(start_url, imgsrc['src'])
                postfix = imgurl.split('/')[-1]
                retry = 3
                while retry > 0:
                    try:
                        imgcontent = requests.get(imgurl, headers = headers, timeout = 5)
                        break
                    except ConnectTimeoutError as e:
                        retry -= 1
                        print (name, "retry", retry)
                        time.sleep(3)
                    except Exception as e:
                        retry = 0
                        print ("just continue")
                else:
                    print ("connect error, just continue")
                    continue
                storedir = os.path.join(basedir, name)
                filename = os.path.join(storedir, postfix)
                if not os.path.exists(storedir):
                    os.makedirs(storedir)
                with open(filename, "wb") as f:
                    f.write(imgcontent.content)
                info = dict()
                info['Spidername'] = 'fishspider'
                info['fromUrl'] = wholeurl
                info['imgurl'] = imgurl
                info['imgsavename'] = filename.split('/')[-1]
                info['width'] = 250
                info['height'] = 250
                info['size'] = 250
                info['type'] = postfix.split('.')[-1]
                info['desc'] = ""
                info['name'] = name
                db.insert_info_one(conn, cur, table, info, basedir)
            print ("finish count", count, "pattern", pattern, "collected", name)
            nset.add(name)
            count = count + 1
            total_count = total_count + 1
            time.sleep(0.5)
    print ("count is", count)
except Exception as e:
    print ("some error", e)
finally:
    conn.commit()
    cur.close()
    conn.close()
    print ("total count is", total_count)
