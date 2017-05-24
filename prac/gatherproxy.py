import requests

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36', 'Host':'www.gatherproxy.com'}

starturl = 'http://www.gatherproxy.com/zh/'

page = requests.get(starturl, headers = headers)



