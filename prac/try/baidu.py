from icrawler.builtin.bing import BingImageCrawler

crawl = BingImageCrawler(parser_threads = 4, downloader_threads = 4, 
        storage = {'root_dir': '/tmp/aa'})
crawl.crawl(keyword = "white shark", max_num = 35)
