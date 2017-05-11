#-*- coding: utf-8 -*-
from icrawler.builtin import BaiduImageCrawler

baidu = BaiduImageCrawler(storage={'root_dir':'/tmp/ac'}, downloader_threads=8)
baidu.crawl(keyword='平行宇宙', offset=0, max_num=1000, min_size=None, max_size=None)
