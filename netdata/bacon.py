from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', db='mysql', charset='utf8')

cur = conn.cursor()
cur.execute('use wikipedia')

def insertPageIfNotExists(url):
    cur.execute("select * from pages where url=%s", (url))
    if cur.rowcount == 0:
        cur.execute('insert into pages (url) values (%s)', (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def insertLink(fromPageId, toPageId):
    cur.execute("select * from links where frompageid = %s and topageid = %s",
            (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("insert into links (fromPageid,  toPageId) values( %s, %s)",
                (int(fromPageId), int(toPageId)))
        conn.commit()

pages = set()
def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return;
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a",
            href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId,
                insertPageIfNotExists(link.attrs['href']))
        if link.attrs['href'] not in pages:
            newPage = link.attrs['href']
            pages.add(newPage)
            getLinks(newPage, recursionLevel+1)
try:
    getLinks("/wiki/Kevin_Bacon", 0)
finally:
    cur.close()
    conn.close()
