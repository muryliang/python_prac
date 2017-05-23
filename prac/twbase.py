import requests
import re
from string import ascii_lowercase
import threading
import pickle
from urllib.parse import urljoin
from lxml.html import fromstring
import os
from requests.exceptions import ConnectionError,ReadTimeout
from requests.exceptions import ReadTimeout
import time
from socket import timeout

starturl = 'http://fishdb.sinica.edu.tw/chi/synonyms_list.php?id=&pz=25&page=0&R1=&key='
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}
ddir = "/tmp/fish" # download base dir

dictionary = dict() # currently do not store any thing
lock = threading.Lock()
index = 0
done = 0 # use this instead of join because join will block, not know why, locked ??
#lst = ['Anguilla marmorata'] # have no internal pic

#get input from csv file
csvfile = "/tmp/fishsorts.dat"
with open(csvfile, "rb") as f:
    fishnames = pickle.load(f)
engname, chiname = fishnames['engname'][:10], fishnames['chiname'][:10]

#get already done set from datafile
datafile = "/tmp/fishexist.dat"
if os.path.exists(datafile):
    with open(datafile, "rb") as f:
        exist_set = pickle.load(f) # exist set
else:
    exist_set = set()

#get no found type's set
notfoundfile = "/tmp/fishnotfound.dat"
if os.path.exists(notfoundfile):
    with open(notfoundfile, "rb") as f:
        notfound_set = pickle.load(f)
else:
    notfound_set = set()

def calculate():
    global total
    global dictionary
    # modify:  这里需要且分传进来的英文中文名，这个中文名比找的要正规
    args = get_next()
    while args is not None:
        print ("start processing",args,"on", threading.currentThread().getName())
        search_str = args[0] # english name
        starturl2 = starturl + "+".join(search_str.split(" "))
        print ("url is", starturl2)

        #should write as a function
        retry = 0
        while  retry < 3:
            try:
                print ("begin try")
                page = requests.get(starturl2, headers = headers, timeout = 5)
                print ("try success")
                break
#            except requests.exceptions.Timeout:
            except Exception as e :
                print ("retry", e)
                retry += 1
                continue
        else:
            print ("requests error, on ", threading.currentThread().getName())
            return

        print ("next")
        infodict = get_info(page, search_str)
        if infodict is None:
            print ("thread", threading.currentThread().getName(),search_str, "already exist")
        elif type(infodict) is int :
            print ("thread", threading.currentThread().getName(), "no result, just continue")
            notfound_set.add(search_str)
        else:
            print ("thread", threading.currentThread().getName(),"get info of %s"%(infodict['name']), infodict)
            infodict['count'] = len(infodict['pictures']) #picture numbers
            print ("get all together %d pictures"%(infodict['count']))
            infodict['中文名'] = args[1]
            dictionary[infodict['name']] = infodict
        args = get_next()
    print ("thread", threading.currentThread().getName(),"done")
    inc_done()

def inc_done():
    global done
    lock.acquire()
    done += 1
    lock.release()

def get_next():
    global index
    lock.acquire()
    if len(engname) != 0:
        next_item = (engname.pop(), chiname.pop())
    else:
        next_item = None
    lock.release()
    return next_item

def get_info(page, search):
    #注意还有原始链接有一张图片，有时候没有内部链接的
    infodict = dict()
    infodict['name'] = search
    if infodict['name'] in exist_set: #already exists
        return None
    else:
        exist_set.add(infodict['name'])

    tree = fromstring(page.text)
    #just search the first, most proper one
    try:
        infodict['valid name'] = tree.xpath("//tr/td[@class='tdN' and @align='left']/a/i/text()")[0].strip()
        xpathstr = "//td/a[./i/text() = \'" + infodict['valid name'] + "\']/@href"
        detailurl = tree.xpath(xpathstr)[0]
    except IndexError as e:
        print ("index error, means that no result, just return")
        return -1
    detailpage = requests.get(urljoin(starturl, detailurl), headers = headers)

    detailtree = fromstring(detailpage.text)
    infodict['pictures'] = []
    try:
        partimgurl = detailtree.xpath("//img[@title='照片']/../@href")[0]
        imgurl = urljoin(starturl, partimgurl)
        infodict['pictures'].extend(get_internal_imgs(imgurl))
    except IndexError as e:
        print ("no internal pictures")
    try:
        fishbaseurl = detailtree.xpath("//img[@title='FishBase']/../@href")[0]
        infodict['pictures'].extend(get_fb_imgs(fishbaseurl))
    except IndexError as e:
        print ("no external pictures")
    download(infodict)
    return infodict

def get_internal_imgs(imgurl):
    inpage = requests.get(imgurl, headers = headers)
    intree = fromstring(inpage.text)
    urllist = intree.xpath("//div[@class='pic']/a/img/@src")
    imgurllist = [urljoin(imgurl, parturl) for parturl in urllist]

    try:
        lasturl = intree.xpath("//div[@class='pic']/a[./div]/@href")[0]
        lastimg = re.match('[^=]*=([^&]*)&.*', lasturl).group(1)
        imgurllist.append(lastimg)
    except IndexError as e:
        print ("no last img, just continue")
    return imgurllist

def get_fb_imgs(imgurl):
    fbpage = requests.get(imgurl, headers = headers)
    fbtree = fromstring(fbpage.text)
    try :
        fbpart = fbtree.xpath("//span[@class='slabel8']/a/@href")[0]
    except IndexError as e:
        print ("error when get img page external, return None")
        return []
    fbimgpage = urljoin(imgurl, fbpart)
    imgpage = requests.get(fbimgpage, headers = headers)
    imgtree = fromstring(imgpage.text)
    picurls = imgtree.xpath("//a[@class='tooltip']/span/img/@src")
    fbpicurls = [ urljoin(imgurl, tmpurl) for tmpurl in picurls]
    return fbpicurls

def download(idict):
    downloaddir = os.path.join(ddir, idict['name'].replace(" ", "_"))
    if not os.path.exists(downloaddir):
        os.makedirs(downloaddir)
    for url in idict['pictures']:
        print ("ready to get img ", url, idict['name'])
        post = url.split('/')[-1].replace(" ", "_").replace("gif", "jpg")
        retry = 0
        while retry < 3:
            try:
                imginfo = requests.get(url, headers = headers)
            except ConnectionError as e:
                print ("encounterred connection error, retry...")
                count += 1
            else:
                break
        print ("success get")
        with open(os.path.join(downloaddir, post), "wb") as f:
            f.write(imginfo.content)
        time.sleep(1)

thread_arr = []
threads = 1
for _ in range(threads):
    t = threading.Thread(target=calculate)
    thread_arr.append(t)
    t.start()

try:
    while index < threads:
        time.sleep(5)
#    for i in range(8):
#        thread_arr[i].join()
finally:
    #print (dictionary)
    with open(datafile, "wb") as f:
        pickle.dump(exist_set, f)
        print ("dump over exist set")
    with open(notfoundfile, "wb") as f:
        pickle.dump(notfound_set, f)
        print ("dump over notfound set")
