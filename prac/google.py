import json
from bs4 import BeautifulSoup
from six.moves.urllib.parse import urlencode
import requests

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'}
base_url = 'https://www.google.com/search?'
for i in range(0,10):
#    cd_min = date_min.strftime('%d/%m/%Y') if date_min else ''
#    cd_max = date_max.strftime('%d/%m/%Y') if date_max else ''
#    tbs = 'cdr:1,cd_min:{},cd_max:{}'.format(cd_min, cd_max)
    params = dict (q=keyword, ijn=int(i / 100), start=0, tbm='isch')
#        q=keyword, ijn=int(i / 100), start=i, tbs=tbs, tbm='isch')
    url = base_url + urlencode(params)
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.text, 'lxml')
    image_divs = soup.find_all('div', class_='rg_meta')
    for div in image_divs:
        meta = json.loads(div.text)
        if 'ou' in meta:
            print ("got", meta['ou'])
    print ("finish page", i / 100, 0)
