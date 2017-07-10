# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from twisted.enterprise import adbapi
from scrapy.exceptions import DropItem
import pymysql
import os
#import re

class MyImagePipeline(ImagesPipeline):

    def __init__(self, store_uri, download_func=None, settings=None):
        super().__init__(store_uri, settings=settings,download_func=download_func)
        self.basedir = settings['IMAGES_STORE']

    def get_media_requests(self, item, info):
#        self.type_name = item['keyword']
        return [Request(x, meta={'itemtype':item['keyword']}) for x in [item[self.images_urls_field],]]

    def item_completed(self, results, item, info):
        image_path_list = [x['path'] for ok, x in results if ok]
        print ("filepaths are ",image_path_list, "and length",len(image_path_list))
        print ("but url path is ", item['objURL'])
        if not image_path_list:
            raise DropItem("Item contains no images")
        item['saveURL'] = image_path_list[0]
        return item;

    def file_path(self, request, response=None, info=None):
        postfix = request.url.split("/")[-1]
        typepath = request.meta['itemtype'].strip().replace(" ","_")
        hashurl = super().file_path(request, response, info)
        filepath = os.path.join(typepath, hashurl.split("/")[-1])
        print ("during file_path, type name is", request.meta['itemtype'])
        return filepath

class StoreMetaPipeline(object):
    def open_spider(self, spider):
        tablename = spider.name
        self.table = self.data['tables'][tablename]

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
        query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item

    def __init__(self, dbpool, data):
        self.dbpool = dbpool
        self.data = data

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        tables = settings['MYSQL_TABLES']
        data = {"tables":tables}
        dbparams = dict(
            host=settings['MYSQL_HOST'],  # 读取settings中的配置
            db=settings['MYSQL_DB'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)  # **表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        return cls(dbpool,data)  # 相当于dbpool付给了这个类，self中可以得到

    # 写入数据库中
    def _conditional_insert(self, tx, item):
        # print item['name']
        sql = "insert ignore into {0} (Spidername, Spiderinfo, fromURL,objURL,saveURL,thumbURL, width,height,size,keyword,type,name,classification,info,gettime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,UNIX_TIMESTAMP())".format(self.table)
        params = (item['Spidername'],item['Spiderinfo'],item['fromURL'],item['objURL'],item['saveURL'],item['thumbURL'],item['width'],item['height'],item['size'],item['keyword'], item['type'],item['name'],item['classification'],item['info'])
        tx.execute(sql, params)

    # 错误处理方法
    def _handle_error(self, failue, item, spider):
        print('--------------database operation exception!!-----------------')
        print('-------------------------------------------------------------')
        print(failue)

