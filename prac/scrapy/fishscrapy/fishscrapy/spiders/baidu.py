from scrapy_redis.spiders import RedisSpider
from fishscrapy.items import FishItem;
import scrapy
import json
import pickle
import socket
import os
import re
import urllib

#class BaiduSpider(scrapy.Spider):
class BaiduSpider(RedisSpider):
    count = 0
    name = "baidu"
    Spidername = name
    redis_key = 'baiduurl'
    base_url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word={0}&cg=girl&pn={1}&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'

    def parse(self, response):
 #       fishtype = response.meta['type']
        fishtype = re.match('.*word=(.*)&cg.*', urllib.parse.unquote(response.url)).group(1)
        imgdict = json.loads(response.text)['imgs']
        for imgmeta in imgdict:
            item = FishItem()
            item['Spidername'] = self.Spidername
            item['Spiderinfo'] = self.getSpiderinfo()
            item['fromURL'] = imgmeta['fromURL']
#            item['thumbURL'] = imgmeta['thumbURL']
            item['thumbURL'] = "none"  #这个是本地的
            item['fromURL'] = imgmeta['fromURL']
            item['objURL'] = imgmeta['objURL']
            item['saveURL'] = "none"
            item['width'] = imgmeta['width']
            item['height'] = imgmeta['height']
            item['type'] = imgmeta['type']
            item['size'] = 0
            item['name'] = imgmeta['objURL'].split('/')[-1]
            item['keyword'] = fishtype
            item['classification'] = fishtype
            item['info'] = "currently none"
            item['count'] = self.count
            self.count += 1
            yield item

    def load_name(self):
        csvfile = "/home/sora/fishsorts.dat"
        with open(csvfile, "rb") as f:
            fishnames = pickle.load(f)
            self.engname = fishnames['chiname']

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

