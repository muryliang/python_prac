from icrawler.builtin.google import GoogleImageCrawler
import pickle
import os

with open("/tmp/fishsorts.dat", "rb") as f:
    fishdict = pickle.load(f)

fishname = fishdict['engname'][:1]
fishname = ['Anacanthobatis_bornneensis']

for i in fishname:
    path = os.path.join("/tmp/aa", "_".join(i.split(" ")))
    crawl = GoogleImageCrawler(parser_threads = 1, downloader_threads = 1, 
                 storage = {'root_dir': path})
    print ("start %s"%(i))
    crawl.crawl(keyword = i, max_num = 50)
