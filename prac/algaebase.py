import requests
import re
from string import ascii_lowercase
import threading
import pickle

starturl = 'http://www.algaebase.org/search/images/'
#headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.5', 'Connection': 'keep-alive', 'Content-Length': '72', 'Content-Type': 'application/x-www-form-urlencoded', 'DNT': '1', 'Host': 'www.algaebase.org', 'Referer': 'http://www.algaebase.org/search/images/', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}

lock = threading.Lock()
total = 0
dictionary = dict()

post_params = {'-Search': 'Search', 'currentMethod': 'imgs', 'displayCount': '20', 'fromSearch': 'yes', 'query': ''}

for arg in ascii_lowercase:
    for j in ascii_lowercase:
        search_str = arg + j
        post_params['query'] = search_str

        try:
            page = requests.post(starturl, data = post_params, headers = headers)
            count = int(re.match('.*<b>([0-9]+)</b> Found.*', str(page.content)).group(1))
        except AttributeError as e:
            print ("AttributeError, continue")
            continue
        total += count
        dictionary[search_str] = count
        print (search_str, " count :", count,"total", total)

print ("total count is", total)
with open("/home/sora/git/python/prac/calfile.dat", "wb") as f:
    pickle.dump(dictionary, f)
    print ("dump over")
