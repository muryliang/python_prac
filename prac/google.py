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
import dbhelper as db
from pymysql.err import ProgrammingError

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
            print ("download failed , just return", inf['imgsavename'])
            retry += 1
            if retry >= 3:
                return False
    with open(filepath, "wb") as f:
        f.write(content.content)
    print ("download pic done", inf['imgsavename'])
    return True

def sigdump(signum, frame):
    print ("begin dump")
#    dump_all()
    sys.exit()

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
    global host
    global user, passwd, dbname, table

    # connect database and create table if needed
    lock.acquire()
    conn, cur = db.get_or_create_db(host, user, passwd, dbname)
    db.create_twtable_if_needed(cur, table)
    lock.release()

    #begin fetch
    curthread = threading.currentThread().getName()
    search_str = get_next()
    while search_str is not None:
        print (curthread, "begin fetching", search_str)

        #load exist data from database
        index_set, exist_set = db.load_exist(cur, search_str, table)
        index = max([int(x.split(".")[0]) for x in index_set], default = -1) + 1
        print ("now start from index ", index)

        #test shows that  only can fetch less than 10 pages, otherwise return no content, so 12 is enough
        for i in range(0,12):
            print ("start loop", i)
            time.sleep(1)

        #    tbs = 'isz:l' #only big size img, but too little
            params = dict (q=search_str, ijn=i , start=i*100, tbm='isch')
            url = base_url + urlencode(params)
            retry = 0
            while retry < 5:
                try:
                    page = requests.get(url, headers = headers)
                    break
                except Exception as e:
                    print ("request get error, retry...")
                    retry += 1
                    time.sleep(2)
            if retry >= 5:
                print ("current url failed", url)
                continue
                        
            soup = BeautifulSoup(page.text, 'lxml')
            image_divs = soup.find_all('div', class_='rg_meta')
            # handle 100 imgs
            for div in image_divs:
                meta = json.loads(div.text)
                #set image's name
                info = dict()
                info['imgsavename'] = str(index) + ".jpg"
                info['desc'] = meta.get('pt', None)
                info['fromUrl'] = meta.get('ru', None)
                info['name'] = search_str
                if 'ou' in meta:
                    info['imgurl'] = meta['ou']
                    info['height'] = meta['oh']
                    info['width'] = meta['ow']
                elif 'tu' in meta:
                    info['imgurl'] = meta['tu']
                    info['height'] = meta['th']
                    info['width'] = meta['tw']
                else:
                    info['imgurl'] = None
                    info['height'] = None
                    info['width'] = None

                if info['imgurl'] in exist_set or info['imgurl'] is None:
                    print ("img %s of %s exists, skip"%(search_str, info['imgurl']))
                    continue
                print ("got image:", info['imgurl'])
                if download_img(info, os.path.join(ddir, search_str.replace(" ", "_"))):
                    print ("finish page", info['imgsavename'])
                    index += 1
                else:
                    print ("skip page", info['imgsavename'])
            #store into db when every species is downloaded
                try:
                    print (curthread, "begin store into database...")
                    lock.acquire()
                    db.insert_info_one(conn, cur, table, info, ddir)
                    lock.release()
                    exist_set.add(info['imgurl'])
                    print (curthread, "finish store into database...")
                except Exception as e:
                    lock.release()
                    conn.commit()
                    cur.close()
                    conn.close()
                    print (e, "exception happened in ",curthread)

            #reopen ,to avoid cursor timeout
            conn.commit()
            cur.close()
            conn.close()
            conn, cur = db.get_or_create_db(host, user, passwd, dbname)
        search_str = get_next()
    print (curthread,"thread done")
    lock_inc()

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'}
base_url = 'https://www.google.com/search?'
dir_prefix = "/mnt/sdb1/fullgoogle"
ddir = os.path.join(dir_prefix, "fishgoogle")
host = "127.0.0.1"
user = "root"
passwd = "123456"
table = "secondgoogletable"
dbname = "fishdb"

#get input from csv file
csvfile = os.path.join(dir_prefix, "fishsort2.dat")
with open(csvfile, "rb") as f:
    fishnames = pickle.load(f)
engname = fishnames['engname'][:]

#daemonize
#set outputfile
stdoutfiletemplate = os.path.join(dir_prefix, "fishgoogle/fishlog")
if not os.path.exists(stdoutfiletemplate):
    os.makedirs(stdoutfiletemplate)
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

while done < threads:
    time.sleep(10)
print ("all threads done")
