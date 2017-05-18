# -*- coding: utf-8 -*-
import scrapy


class ExpSpider(scrapy.Spider):
    name = "exp"
    allowed_domains = ["www.baidu.com"]
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
