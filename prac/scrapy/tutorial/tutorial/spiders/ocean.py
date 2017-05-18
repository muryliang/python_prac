import scrapy
import re
import requests
import os

class Ocean(scrapy.Spider):
    name = "ocean"

    start_urls = ['http://oceana.org/marine-life/marine-mammals/harp-seal?combine=&page=0',
        'http://oceana.org/marine-life/marine-mammals/harp-seal?combine=&page=1',
        'http://oceana.org/marine-life/marine-mammals/harp-seal?combine=&page=2',
        ]

    def parse(self, response):
        print ("get url:", response.url)
        url = response.url
        if re.match('http://oceana.org/marine-life/marine-mammals/harp-seal\?combine.*', url): # first layer
            urllist = response.xpath('//div[@class="inner-contain animal-list"]//a/@href').extract()
            for suburl in urllist:
                next_page = response.urljoin(suburl)
                yield scrapy.Request(next_page, callback=self.parse)

        else:
            imgurl = response.xpath('//link[@rel="image_src"]/@href').extract_first()
            with open("hehe", 'a+') as f:
                f.write(""+imgurl+"\n")
            imgpostfix = imgurl.split("/")[-1]
            homedir="/home/sora/pic"
            if not os.path.exists(homedir):
                os.makedirs(homedir)
            imgpath = os.path.join(homedir, imgpostfix)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
            response = requests.get(imgurl, headers=headers)
            with open(imgpath, "wb") as f:
                f.write(response.content)
                f.flush()
