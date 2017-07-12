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
from lxml.html import fromstring

#class BaiduSpider(scrapy.Spider):
class algaebaseSpider(RedisSpider):
    count = 0
    name = "algaebase"
    Spidername = name
    redis_key = 'algaebaseurl'

    def parse(self, response):
        fishtype = response.meta['type']
        tree = fromstring(response.text)

#        with open("/tmp/list2.html" ,"w") as f:
#            f.write(response.text)
        try:
            searchurl = tree.xpath("//td/p/a[contains(@href,'search')]/@href")[0]
            name = tree.xpath("//td/p/a[contains(@href,'search')]/text()")[0]
            name = name.split(" ")[0] + name.split(" ")[1]
            #thumbnails are tree.xpath("//td/p/a/img/@src")
            if name.strip().replace(" ","").lower() == fishtype.strip().replace(" ", "").lower():
                yield response.follow(searchurl, meta = {'type':fishtype}, callback = self.detailparse)
            else:
                print ("name not same", name.strip().replace(" ","").lower(), fishtype.strip().replace(" ", "").lower())
                return None
        except IndexError as e:
            print ("search no found, skip ", response.url, response.status)
            return None

    def detailparse(self, response):
        fishtype = response.meta['type']
        tree = fromstring(response.text)

        #parse first 10 pictures
        pictureurls = tree.xpath("//p[@class='speciesimages']/a/@href")
        for item in self.parse_pictures(response.url, pictureurls, fishtype):
            yield item
        for url in tree.xpath("//p/a/@href"):
            if "sk=" in url:
                yield scrapy.Request(urllib.parse.urljoin(response.url, url), 
                        meta={'type':fishtype}, callback=self.picparse)

    def picparse(self, response):
        fishtype = response.meta['type']
        tree = fromstring(response.text)
        pictureurls = tree.xpath("//p[@class='speciesimages']/a/@href")
        print ("begin parse pictures")
        for item in self.parse_pictures(response.url, pictureurls, fishtype):
            yield item

    def parse_pictures(self, fromurl, urllist, fishtype):
        print ("now in item processing")
        for url in urllist:
            item = FishItem()
            item['Spidername'] = self.Spidername
            item['Spiderinfo'] = self.getSpiderinfo()
            item['fromURL'] = fromurl
#            item['thumbURL'] = imgmeta['thumbURL']
            item['thumbURL'] = "none"  #这个是本地的
            item['objURL'] = url
            item['saveURL'] = "none"
            item['width'] = 0
            item['height'] = 0
            item['type'] = item['objURL'].split(".")[-1]
            item['size'] = 0
            item['name'] = item['objURL'].split('/')[-1]
            item['keyword'] = fishtype
            item['classification'] = fishtype
            item['info'] = "currently none"
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
        print ("start to process")
        datastr = bytes_to_str(data, self.redis_encoding)
        base_url, fishtype = [a.strip() for a in datastr.split(",")]
        formdata = {'currentMethod':'imgs', 'fromSearch':'yes','displayCount':'200','query':fishtype,'-Search':'Search'}
        return scrapy.FormRequest(url=base_url, meta = {'type':fishtype},
                callback=self.parse, formdata = formdata, dont_filter=True) 
