# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FishItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    picid = scrapy.Field()
    Spidername = scrapy.Field()
    Spiderinfo = scrapy.Field()
    fromURL = scrapy.Field()
    objURL = scrapy.Field()
    saveURL = scrapy.Field()
    thumbURL = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    size = scrapy.Field()
    type = scrapy.Field()
    name = scrapy.Field()
    keyword = scrapy.Field();
    classification = scrapy.Field()
    info = scrapy.Field()
    #time is autoinsert
    #gettime = scrapy.Field()
    images = scrapy.Field()
