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
from lxml.html import fromstring

class GoogleSpider(RedisSpider):
    count = 0
    name = "google"
    Spidername = name
    redis_key = 'googleurl'

    def parse(self, response):
 #       fishtype = response.meta['type']
        fishtype = re.match('.*q=(.*)&ijn.*', urllib.parse.unquote(response.url)).group(1).replace("+"," ")
        tree = fromstring(response.text)
        imgmetas = tree.xpath("//div[contains(@class, 'rg_meta')]")
        for imgmeta in imgmetas:
            meta = json.loads(imgmeta.text)
            item = FishItem()
            item['Spidername'] = self.Spidername
            item['Spiderinfo'] = self.getSpiderinfo()
            item['fromURL'] = meta.get('ru', "none")
#            item['thumbURL'] = imgmeta['thumbURL']
            item['thumbURL'] = "none"  #这个是本地的
            if 'ou' in meta:
                item['objURL'] = meta['ou']
                item['height'] = meta['oh']
                item['width'] = meta['ow']
            elif 'tu' in meta:
                item['objURL'] = meta['tu']
                item['height'] = meta['th']
                item['width'] = meta['tw']
            else:
                item['objURL'] = ""
                item['height'] = 0
                item['width'] = 0
            item['saveURL'] = "none"
            item['type'] = meta.get('ity','none')
            item['size'] = 0
            item['name'] = item['objURL'].split('/')[-1]
            item['keyword'] = fishtype
            item['classification'] = fishtype
            item['info'] = meta.get('pt', 'none')
            item['count'] = self.count
            self.count += 1
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

