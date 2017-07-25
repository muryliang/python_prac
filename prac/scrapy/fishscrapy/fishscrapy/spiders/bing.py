from scrapy_redis.spiders import RedisSpider
from scrapy_redis.utils import bytes_to_str
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

class BingSpider(RedisSpider):
    count = 0
    name = "bing"
    Spidername = name
    redis_key = 'bingurl'

    def parse(self, response):
        fishtype = re.match('.*q=(.*)&first.*', urllib.parse.unquote(response.url)).group(1)
        tree = fromstring(response.text)
        dictlist = tree.xpath("//div[@class='imgpt']/a/@m")
        imgmetas = [json.loads(x) for x in dictlist]
        sizelist = tree.xpath("//div[@class='imgpt']/a/@style")
        sizemeta = [(x.split(';')[0].split(':')[1].rstrip('px'), x.split(';')[1].split(':')[1].rstrip('px')) for x in sizelist]
        for siz, meta in zip(sizemeta, imgmetas):
            item = FishItem()
            item['Spidername'] = self.Spidername
            item['Spiderinfo'] = self.getSpiderinfo()
            item['fromURL'] = meta['purl']
#            item['thumbURL'] = imgmeta['thumbURL']
            item['thumbURL'] = "none"  #这个是本地的
            item['objURL'] = meta['murl']
            item['height'] = int(siz[0])
            item['width'] = int(siz[1])
            item['saveURL'] = "none"
            item['type'] = meta['murl'].split('.')[-1]
            item['size'] = 0
            item['name'] = item['objURL'].split('/')[-1]
            item['keyword'] = fishtype
            item['classification'] = fishtype
            item['info'] = ""
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

    def make_request_from_data(self, data):
        """override method"""
        base_url = bytes_to_str(data, self.redis_encoding)
        return scrapy.Request(url=base_url, dont_filter=True) 

