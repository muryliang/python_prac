# -*- coding: utf-8 -*-
import scrapy
from fishimg.items import FishimgItem
import requests
from requests.exceptions import ConnectionError,ReadTimeout
from requests.exceptions import ReadTimeout
from urllib.parse import urljoin
from lxml.html import fromstring
import re
import threading
import pickle
import os
import sys
import time
import signal



class FishimgSpider(scrapy.Spider):
    name = "musofish"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}
    baseurl = 'http://fishdb.sinica.edu.tw/chi/synonyms_list.php?id=&pz=25&page=0&R1=&key='
    ddir = "/mnt/sdb1/twscrapy"
#    start_urls = ['http://example.com/']
    
    def start_requests(self):
        self.load_name()
        for name in self.engnames[:10]:
            print ("begin for name %s"%(name))
            yield scrapy.Request(url = self.baseurl + "+".join(name.split(" ")))

    def parse(self, response):
        name = re.match( '.*&key=(.*)$', response.url).group(1).strip().replace("+", " ")
        tree = fromstring(response.text)

        try:
            validname = tree.xpath("//tr/td[@class='tdN' and @align='left']/a/i/text()")[0].strip()
            xpathstr = "//td/a[./i/text() = \'" + validname + "\']/@href"
            fromurl = tree.xpath(xpathstr)[0]
        except IndexError as e:
            print ("index error, means that no result, just return", name)
            return None
        detailpage = requests.get(urljoin(self.baseurl, fromurl), headers = self.headers)
        detailtree = fromstring(detailpage.text)
        pictures = list()
        try:
            partimgurl = detailtree.xpath("//img[@title='照片']/../@href")[0]
            imgurl = urljoin(self.baseurl, partimgurl)
            pictures.extend(self.get_internal_imgs(imgurl))
        except IndexError as e:
            print ("no internal pictures")
        try:
            fishbaseurl = detailtree.xpath("//img[@title='FishBase']/../@href")[0]
            pictures.extend(self.get_fb_imgs(fishbaseurl))
        except IndexError as e:
            print ("no external pictures")
#        self.download_img(pictures, name, fromurl)
        downloaddir = os.path.join(self.ddir, name.replace(" ", "_"))
        if not os.path.exists(downloaddir):
            os.makedirs(downloaddir)
        for url in pictures:
            print ("ready to get img ", url, name)
            post = url.split('/')[-1].replace(" ", "_").replace("gif", "jpg")
            retry = 0
            while retry < 3:
                try:
                    imginfo = requests.get(url, headers = self.headers)
                    print ("sucess get img", imginfo)
                except ConnectionError as e:
                    print ("encounterred connection error, retry...")
                    retry += 1
                else:
                    break
            else:
                print (" %s  for %s get error, skip"%(url, name))
                continue
            print ("going to get image")
            with open(os.path.join(downloaddir, post), "wb") as f:
                f.write(imginfo.content)
            item = FishimgItem()
            item['name'] = post
            item['fromURL'] = fromurl
            item['objURL'] = url
            item['keyword'] = name
            item['Spidername'] = 'twfish'
            item['type'] = 'jpg'
            item['size'] = imginfo.content.__sizeof__()
            item['width'] = 0
            item['height'] = 0
            item['saveURL'] = os.path.join(downloaddir, post)
            item['classification'] = ''
            item['info'] = ''
            print ("success get %s and write into %s"%(name, post))
            yield item
            time.sleep(0.5)

    def get_internal_imgs(self, imgurl):
        inpage = requests.get(imgurl, headers = self.headers)
        intree = fromstring(inpage.text)
        urllist = intree.xpath("//div[@class='pic']/a/img/@src")
        imgurllist = [urljoin(imgurl, parturl) for parturl in urllist]

        try:
            lasturl = intree.xpath("//div[@class='pic']/a[./div]/@href")[0]
            lastimg = re.match('[^=]*=([^&]*)&.*', lasturl).group(1)
            imgurllist.append(lastimg)
        except IndexError as e:
            print ("no last img, just continue")
        return imgurllist

    def get_fb_imgs(self, imgurl):
        fbpage = requests.get(imgurl, headers = self.headers)
        fbtree = fromstring(fbpage.text)
        try :
            fbpart = fbtree.xpath("//span[@class='slabel8']/a/@href")[0]
        except IndexError as e:
            print ("error when get img page external, return None")
            return []
        fbimgpage = urljoin(imgurl, fbpart)
        imgpage = requests.get(fbimgpage, headers = self.headers)
        imgtree = fromstring(imgpage.text)
        picurls = imgtree.xpath("//a[@class='tooltip']/span/img/@src")
        fbpicurls = [ urljoin(imgurl, tmpurl) for tmpurl in picurls]
        return fbpicurls

    def download_img(self, pics, name, fromurl):
        downloaddir = os.path.join(self.ddir, name.replace(" ", "_"))
        if not os.path.exists(downloaddir):
            os.makedirs(downloaddir)
        for url in pics:
            print ("ready to get img ", url, name)
            post = url.split('/')[-1].replace(" ", "_").replace("gif", "jpg")
            retry = 0
            while retry < 3:
                try:
                    imginfo = requests.get(url, headers = self.headers)
                    print ("sucess get img", imginfo)
                except ConnectionError as e:
                    print ("encounterred connection error, retry...")
                    retry += 1
                else:
                    break
            else:
                print (" %s  for %s get error, skip"%(url, name))
                continue
            print ("going to get image")
            with open(os.path.join(downloaddir, post), "wb") as f:
                f.write(imginfo.content)
            item = FishimgItem()
            item['name'] = post
            item['fromURL'] = fromurl
            item['objURL'] = url
            item['keyword'] = name
            item['Spidername'] = 'twfish'
            item['type'] = 'jpg'
            item['size'] = imginfo.content.__sizeof__()
            item['saveURL'] = os.path.join(downloaddir, post)
            print ("success get %s and write into %s"%(name, post))
            yield item
            time.sleep(0.5)

    def load_name(self):
        csvfile = "/home/sora/fishsorts.dat"
        with open(csvfile, "rb") as f:
            fishnames = pickle.load(f)
            self.engnames = fishnames['engname']

