import scrapy
import os
from urllib.request import urlretrieve

class QuotesSpider(scrapy.Spider):
    name = "quotes2"

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        urls = [
                'http://site1.zjou.edu.cn/fish/uploadimg1/',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers = headers)

    def parse(self, response):
        urllist = response.xpath("//a/@href").extract()
        for url in urllist:
            if url.endswith("/"):
                continue
            postfix = url.split("/")[-1]
            filename = os.path.join("/home/sora/shell_pic", postfix)
            hurl = response.urljoin(url)
            if not os.path.exists(filename):
                print (hurl, filename)
                urlretrieve(hurl, filename)
                print ("saved %s" %(postfix))
            else:
                print ("pass", filename)
