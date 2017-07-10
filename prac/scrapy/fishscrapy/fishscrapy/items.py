# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


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
    count = scrapy.Field()

class FishLoader(ItemLoader):
    default_item_class = FishItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
