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

class fishbaseSpider(RedisSpider):
    count = 0
    name = "fishbase"
    Spidername = name
    redis_key = 'fishbaseurl'

    def parse(self, response):
        print ("url is ",urllib.parse.unquote(response.request.url))
        types = re.match('.*genusname=(.*)&speciesname=(.*)&lang=Chinese$', urllib.parse.unquote(response.request.url))
        if not types  or not types.group(1) or not types.group(2):
            print (response.request.url,"can not parse")
            return None
        fishtype = types.group(1) + " " + types.group(2)

        fbtree = fromstring(response.text)
        try :
            fbpart = fbtree.xpath("//span[@class='slabel8']/a/@href")[0]
        except IndexError as e:
            print ("error when get img page external")
            return None

        yield response.follow(fbpart, meta = {'type':fishtype}, callback = self.imageparse)

    def imageparse(self, response):
        fishtype = response.meta['type']
        imgtree = fromstring(response.text)
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
            item['info'] = 'none'
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

