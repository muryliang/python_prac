from icrawler.builtin.baidu import BaiduImageCrawler

crawl = BaiduImageCrawler(parser_threads = 4, downloader_threads = 4, 
        storage = {'root_dir': '/tmp/aa'})
crawl.crawl(keyword = "小人", max_num = 500)
