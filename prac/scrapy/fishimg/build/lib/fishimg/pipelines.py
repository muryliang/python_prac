# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import pymysql

class FishimgPipeline(object):

    def process_item(self, item, spider):
        print ("begin inserting database")
        query = self.dbpool.runInteraction(self._conditional_insert, item)  # 调用插入的方法
        query.addErrback(self._handle_error, item, spider)  # 调用异常处理方法
        return item

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
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
        return cls(dbpool)  # 相当于dbpool付给了这个类，self中可以得到

    # 写入数据库中
    def _conditional_insert(self, tx, item):
        # print item['name']
        sql = "insert into twtable (Spidername, fromURL,objURL,saveURL,width,height,size,keyword,type,name,classification,info,gettime)" \
              " values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,UNIX_TIMESTAMP())"
        #print('chk insert sql:', sql)
        if(item['width'] is None):
            item['width'] = 0
        if (item['height'] is None ):
            item['height'] = 0
        if (item['size'] is None ):
            item['size'] = 0
        params = (item['Spidername'],item['fromURL'],item['objURL'],item['saveURL'],item['width'],item['height'],item['size'],item['keyword'], item['type'],item['name'],item['classification'],item['info'])
        tx.execute(sql, params)
        print ("finish insert %s, %s"%(item['name'], item['keyword']))

    # 错误处理方法
    def _handle_error(self, failue, item, spider):
        print('--------------database operation exception!!-----------------')
        print('-------------------------------------------------------------')
        print(failue)

