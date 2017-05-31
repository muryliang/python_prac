import json
from bs4 import BeautifulSoup
from six.moves.urllib.parse import urlencode
import requests
import time
import pickle
import os
import sys
import threading
import signal

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

def download_img(inf, ddir):
    global headers
    if not os.path.exists(ddir):
        os.makedirs(ddir)
    filepath = os.path.join(ddir, inf['imgsavename'])
    retry = 0
    while retry < 3:
        try:
            content = requests.get(inf['imgurl'], headers = headers, timeout = 5)
            break
        except Exception as e:
            print (threading.currentThread().getName(), "download failed , just return", inf['imgsavename'])
            retry += 1
            if retry >= 3:
                return False
    with open(filepath, "wb") as f:
        f.write(content.content)
    print (threading.currentThread().getName(), "download pic done", inf['imgsavename'])
    return True

def sigdump(signum, frame):
    print ("begin dump")
    dump_all()
    sys.exit()

def dump_all():
    global exist_set
    global existfile
    global alldict
    global dumpfile
    global lock
    lock.acquire()
    with open(dumpfile, "wb") as f:
        pickle.dump(alldict, f)
    with open(existfile, "wb") as f:
        pickle.dump(exist_set, f)
    lock.release()

def lock_inc():
    global done
    global lock
    lock.acquire()
    done += 1
    lock.release()

def get_next():
    global lock
    global engname
    lock.acquire()
    if len(engname) != 0:
        next_item = engname.pop()
    else:
        next_item = None
    lock.release()
    return next_item

def calculate():
    global ddir
    search_str = get_next()
    curthread = threading.currentThread().getName()
    while search_str is not None:
        if search_str.replace(" ", "_") in exist_set:
            print (curthread,"already downloaded", search_str)
            search_str = get_next()
            continue
        print (curthread, "begin fetching", search_str)
        info = dict() # this for one species
        index = 0
        #test shows that  only can fetch less than 10 pages, otherwise return no content, so 12 is enough
        for pn in range(0,840, 60):
            print (threading.currentThread().getName(), "start loop", pn // 60)
            time.sleep(1)

        #    tbs = 'isz:l' #only big size img, but too little
#            params = dict (q=search_str, ijn=i , start=i*100, tbm='isch')
            url = base_url.format(search_str, str(pn))
            print (threading.currentThread().getName(), "begin try url", url)
            retry = 0
            while retry < 5:
                try:
                    page = requests.get(url, headers = headers)
                    break
                except Exception as e:
                    print (threading.currentThread().getName(), "request get error, retry...")
                    retry += 1
                    time.sleep(2)
            if retry >= 5:
                print (threading.currentThread().getName(), "current url failed", url)
                continue
                        
            json_data = json.loads(page.text)
            # handle 100 imgs
            for div in json_data['imgs']:
                #set image's name
                info[index] = dict()
                info[index]['imgsavename'] = str(index) + ".jpg"
                info[index]['fromURL'] = div['fromURL']
                info[index]['fromURLHost'] = div['fromURLHost']
                info[index]['name'] = search_str
                info[index]['width'] = div['width']
                info[index]['height'] = div['height']
                info[index]['imgurl'] = div['objURL']
                info[index]['filesize'] = div['filesize']
                info[index]['pageNum'] = div['pageNum']
                info[index]['bdImgnewsDate'] = div['bdImgnewsDate']
                info[index]['fromPageTitle'] = div['fromPageTitle']
                info[index]['type'] = div['type']

                print (threading.currentThread().getName(), "got image:", info[index]['imgurl'])
                if download_img(info[index], os.path.join(ddir, search_str.replace(" ", "_"))):
                    print (threading.currentThread().getName(), "finish page", info[index]['imgsavename'])
                    index += 1
                else:
                    print (threading.currentThread().getName(), "skip page", info[index]['imgsavename'])
                # peirodically backup
                if index % 100 == 99:
                    dump_all()
        lock.acquire()
        alldict[search_str] = info
        exist_set.add(search_str.replace(" ", "_"))
        lock.release()
        search_str = get_next()
    print (curthread,"thread done")
    lock_inc()

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'}
base_url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word={0}&cg=girl&pn={1}&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
dir_prefix = "/mnt/sdb1/bbaadd"
ddir = os.path.join(dir_prefix, "fishgoogle")
#global dictionary, used to be stored and read

#get input from csv file
csvfile = os.path.join(dir_prefix, "fishsorts.dat")
with open(csvfile, "rb") as f:
    fishnames = pickle.load(f)
engname = fishnames['chiname'][:500]

#search_str = "Cololabis saira"
existfile = os.path.join(dir_prefix, "fishgoogle/exist.dat")
if os.path.exists(existfile):
    print ("read exist")
    with open(existfile, "rb") as f:
        exist_set = pickle.load(f) # exist set
#    print ("exist is", exist_set)
else:
    exist_set = set()

dumpfile = os.path.join(dir_prefix, "fishgoogle/dumpfish.dat")
if os.path.exists(dumpfile):
    print ("read exist")
    with open(dumpfile, "rb") as f:
        alldict = pickle.load(f) # exist set
else:
    alldict = dict()

#daemonize
#set outputfile
stdoutfiletemplate = os.path.join(dir_prefix, "fishgoogle/fishlog")
outfile = stdoutfiletemplate + "-" + time.strftime("%Y%m%d-%H%M%S")
open(outfile, "w").close()

#daemon your process
daemonize(stdout= outfile, stderr= outfile)


#set signal
signal.signal(signal.SIGTERM, sigdump)
signal.signal(signal.SIGINT, sigdump)

#about thread manage
done = 0
lock = threading.Lock()
thread_arr = []
threads = 4
for _ in range(threads):
    t = threading.Thread(target=calculate)
    thread_arr.append(t)
    t.start()

try:
    while done < threads:
        time.sleep(10)
    print ("all threads done")
finally:
    dump_all()
