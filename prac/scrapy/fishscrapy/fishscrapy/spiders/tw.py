from scrapy_redis.spiders import RedisSpider
from fishscrapy.items import FishItem;
import scrapy
import json
import pickle
import socket
import os
import re
import urllib
import json
import requests
from lxml.html import fromstring
from urllib.parse import urljoin
from urllib.request import urlopen, Request

class TwSpider(RedisSpider):
    count = 0
    name = "tw"
    Spidername = name
    redis_key = 'twurl'
    custom_settings = {
            'CONCURRENT_REQUESTS':4,
    }
    myheader = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}

    def parse(self, response):
        fishtype = re.match('.*key=(.*)$', urllib.parse.unquote(response.url)).group(1).replace("+"," ")
        tree = fromstring(response.text)
        try:
            valid_name = tree.xpath("//tr/td[@class='tdN' and @align='left']/a/i/text()")[0].strip()
            xpathstr = "//td/a[./i/text() = \'" + valid_name + "\']/@href"
            detailurl = tree.xpath(xpathstr)[0]
            #response.follow(detailurl, callback=detailParse, meta={'type':fishtype,})
            # scrapy and requests module can not get description info, use urllib instead
            req = Request(urljoin(response.url, detailurl), headers=self.myheader)
            content = urlopen(req).read().decode('utf-8')
        except IndexError as e:
            print ("index error, means that no result")
            return None

        detailtree = fromstring(content)
        infostr = str()
        for info in detailtree.xpath("//td[contains(@class, 'tdsp')]"):
            infostr += str(info.text_content().strip())+' '
        infostr = re.sub('\s+', ' ', infostr)

        # internal images
        try:
            partimgurl = detailtree.xpath("//img[@title='照片']/../@href")[0]
            imgurl = urljoin(response.url, partimgurl)
            yield scrapy.Request(imgurl, callback=self.process_internal_images, 
                    meta={'type':fishtype, 'infostr':infostr})
        except IndexError as e:
            print ("no internal pictures for ", fishtype)

        #fishbase images
        try:
            fishbaseurl = detailtree.xpath("//img[@title='FishBase']/../@href")[0]
            yield scrapy.Request(fishbaseurl, self.process_external_images, 
                meta={'type':fishtype, 'infostr':infostr})
        except IndexError as e:
            print ("no external pictures for ", fishtype)

    def process_internal_images(self, response):
        fishtype = response.meta['type']
        infostr = response.meta['infostr']

        intree = fromstring(response.text)
        urllist = intree.xpath("//div[@class='pic']/a/img/@src")
        imgurllist = [urljoin(response.url, parturl) for parturl in urllist]

        #get last image if exists
        try:
            lasturl = intree.xpath("//div[@class='pic']/a[./div]/@href")[0]
            lastimg = re.match('[^=]*=([^&]*)&.*', lasturl).group(1)
            imgurllist.append(lastimg)
        except IndexError as e:
            print ("no last img, just continue")

        spiderinfo = self.getSpiderinfo()
        for imgurl in imgurllist:
            item = FishItem()
            item['Spidername'] = self.Spidername
            item['Spiderinfo'] = spiderinfo
            item['fromURL'] = response.url
#            item['thumbURL'] = imgmeta['thumbURL']
            item['thumbURL'] = "none"  #这个是本地的
            item['objURL'] = imgurl
            item['height'] = 0
            item['width'] = 0
            item['size'] = 0
            item['saveURL'] = "none"
            item['type'] = item['objURL'].split('.')[-1]
            item['name'] = item['objURL'].split('/')[-1]
            item['keyword'] = fishtype
            item['classification'] = fishtype
            item['info'] = infostr
            item['count'] = 0 # not used in tw
            yield item

    def process_external_images(self, response):
        fishtype = response.meta['type']
        infostr = response.meta['infostr']
        fbtree = fromstring(response.text)
        try :
            fbpart = fbtree.xpath("//span[@class='slabel8']/a/@href")[0]
        except IndexError as e:
            print ("error when get img page external")
            return None # is this needed?

        fbimgpage = urljoin(response.url, fbpart)
        imgpage = requests.get(urljoin(response.url, fbpart), headers = self.myheader)
        imgtree = fromstring(imgpage.text)
        picurls = imgtree.xpath("//a[@class='tooltip']/span/img/@src")
        fbpicurls = [urljoin(response.url, tmpurl) for tmpurl in picurls]
        spiderinfo = self.getSpiderinfo()
        for imgurl in fbpicurls:
            item = FishItem()
            item['Spidername'] = self.Spidername
            item['Spiderinfo'] = spiderinfo
            item['fromURL'] = response.url
#            item['thumbURL'] = imgmeta['thumbURL']
            item['thumbURL'] = "none"  #这个是本地的
            item['objURL'] = imgurl
            item['height'] = 0
            item['width'] = 0
            item['size'] = 0
            item['saveURL'] = "none"
            item['type'] = item['objURL'].split('.')[-1]
            item['name'] = item['objURL'].split('/')[-1]
            item['keyword'] = fishtype
            item['classification'] = fishtype
            item['info'] = infostr
            item['count'] = 0 # not used in tw
            yield item

    def getSpiderinfo(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('www.baidu.com',0))
            ip=s.getsockname()[0]
        except:
            ip=""
        finally:
            s.close()
        pid = os.getpid()
        infostr="pid: %s; ip: %s;"%(pid, ip)
        return infostr

