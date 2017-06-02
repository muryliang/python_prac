import requests
from requests.exceptions import ConnectionError,ReadTimeout
from requests.exceptions import ReadTimeout
from urllib.parse import urljoin
from lxml.html import fromstring
import re
import threading
import pickle
import os
import sys
import time
import signal

starturl = 'http://fishdb.sinica.edu.tw/chi/synonyms_list.php?id=&pz=25&page=0&R1=&key='
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}
ddir = "/home/jztec/fish2" # download base dir

lock = threading.Lock()
index = 0
done = 0 # use this instead of join because join will block, not know why, locked ??
#lst = ['Anguilla marmorata'] # have no internal pic
stdoutfiletemplate = os.path.join(ddir, "fishlog")

#get input from csv file
csvfile = os.path.join(ddir,"fishsorts.dat")
with open(csvfile, "rb") as f:
    fishnames = pickle.load(f)
engname, chiname = fishnames['engname'][:], fishnames['chiname'][:]

#get already done set from datafile
datafile = os.path.join(ddir, "fishexist.dat")
if os.path.exists(datafile):
    print ("read exist")
    with open(datafile, "rb") as f:
        exist_set = pickle.load(f) # exist set
    print ("exist is", exist_set)
else:
    exist_set = set()

#get no found type's set
notfoundfile = os.path.join(ddir, "fishnotfound.dat")
if os.path.exists(notfoundfile):
    with open(notfoundfile, "rb") as f:
        notfound_set = pickle.load(f)
else:
    notfound_set = set()

fishmetafile = os.path.join(ddir, "fishmeta.dat")
if os.path.exists(fishmetafile):
    with open(fishmetafile, "rb") as f:
        dictionary = pickle.load(f)
else:
    dictionary = dict() # currently do not store any thing

def calculate():
    global total
    global dictionary
    global index
    # modify:  这里需要且分传进来的英文中文名，这个中文名比找的要正规
    args = get_next()
    while args is not None:
        print ("start processing",args,"on", threading.currentThread().getName())
        search_str = args[0] # english name
        if search_str.replace(" ","_") in exist_set: #already exists
            print ("thread", threading.currentThread().getName(),search_str, "already exist")
            args = get_next()
            continue
        elif search_str in notfound_set:
            print ("thread", threading.currentThread().getName(),search_str, "previously not found")
            args = get_next()
            continue

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
                time.sleep(1)
                continue
        else:
            print ("requests error, on ", threading.currentThread().getName())
            return

        infodict = get_info(page, search_str)
        if type(infodict) is int :
            print ("thread", threading.currentThread().getName(), "no result, just continue")
            notfound_set.add(search_str)
        else:
            print ("thread", threading.currentThread().getName(),"get info of %s"%(infodict['name']), infodict)
            infodict['count'] = len(infodict['pictures']) #picture numbers
            print ("get all together %d pictures"%(infodict['count']))
#            infodict['中文名'] = args[1]
            dictionary[infodict['name']] = infodict
            exist_set.add(infodict['name'].replace(" ", "_"))
        args = get_next()

        #temply save in case of accident
        if index  == 19:
            lock.acquire()
            dump_all()
            lock.release()
        index = (index + 1) % 20

    print ("thread", threading.currentThread().getName(),"done")
    inc_done()

def inc_done():
    global done
    lock.acquire()
    done += 1
    lock.release()

def get_next():
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

    tree = fromstring(page.text)
    #just search the first, most proper one
    try:
        infodict['valid name'] = tree.xpath("//tr/td[@class='tdN' and @align='left']/a/i/text()")[0].strip()
        xpathstr = "//td/a[./i/text() = \'" + infodict['valid name'] + "\']/@href"
        detailurl = tree.xpath(xpathstr)[0]
        infodict['fishinfourl'] = detailurl
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
        infodict['internalimgurl'] = imgurl
    except IndexError as e:
        infodict['internalimgurl'] = None
        print ("no internal pictures")
    try:
        fishbaseurl = detailtree.xpath("//img[@title='FishBase']/../@href")[0]
        infodict['pictures'].extend(get_fb_imgs(fishbaseurl))
        infodict['externalimgurl'] = fishbaseurl
    except IndexError as e:
        print ("no external pictures")
        infodict['externalimgurl'] = None
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
                retry += 1
            else:
                break
        print ("success get")
        with open(os.path.join(downloaddir, post), "wb") as f:
            f.write(imginfo.content)
        time.sleep(1)

def daemonize(stdin='/dev/null',stdout= '/dev/null', stderr= 'dev/null'):
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0) #first parent out
    except OSError as  e:
        sys.stderr.write("fork #1 failed: (%d) %s\n" %(e.errno, e.strerror))
        sys.exit(1)

    #从母体环境脱离
    os.chdir("/")
    os.umask(0)
    os.setsid()
    #执行第二次fork
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0) #second parent out
    except OSError as  e:
        sys.stderr.write("fork #2 failed: (%d) %s]n" %(e.errno,e.strerror))
        sys.exit(1)

#进程已经是守护进程了，重定向标准文件描述符
    for f in sys.stdout, sys.stderr: f.flush()
    si = open(stdin, 'rb')
    so = open(stdout,'ab+')
    se = open(stderr,'ab+',0)
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

def dump_all():
    global datafile
    global notfoundfile
    global notfound_set
    global exist_set
    global fishmetafile
    global dictionary
    with open(datafile, "wb") as f:
        pickle.dump(exist_set, f)
        print ("dump over exist set")
    with open(notfoundfile, "wb") as f:
        pickle.dump(notfound_set, f)
        print ("dump over notfound set")
    with open(fishmetafile, "wb") as f:
        pickle.dump(dictionary, f)
        print ("dump over dictionary")

def sigdump(signum, frame):
    lock.acquire()
    dump_all()
    lock.release()
    sys.exit()

#set outputfile
outfile = stdoutfiletemplate + "-" + time.strftime("%Y%m%d-%H%M%S")
open(outfile, "w").close()

#daemon your process
daemonize(stdout= outfile, stderr= outfile)

#set signal function
signal.signal(signal.SIGTERM, sigdump)
signal.signal(signal.SIGINT, sigdump)

#start thread
thread_arr = []
threads = 6
for _ in range(threads):
    t = threading.Thread(target=calculate)
    thread_arr.append(t)
    t.start()

try:
    while done < threads:
        time.sleep(10)
# join 有一些问题，会block，这里就不join了，利用done计数探测是否结束所有线程
#    for i in range(8):
#        thread_arr[i].join()
finally:
    #print (dictionary)
    dump_all()
