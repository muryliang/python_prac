#-*- coding: utf-8 -*-
from icrawler.builtin import GoogleImageCrawler, BaiduImageCrawler

baidu = GoogleImageCrawler(storage={'root_dir':'/tmp/ac'}, downloader_threads=8)
baidu.crawl(keyword='super', offset=0, max_num=1000, min_size=None, max_size=None)
