# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FishimgItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    fromURL = scrapy.Field()
    objURL = scrapy.Field()
    Spidername = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    size = scrapy.Field()
    type = scrapy.Field()
    keyword = scrapy.Field()
    classification = scrapy.Field()
    gettime = scrapy.Field()
    info = scrapy.Field()
    saveURL = scrapy.Field()
