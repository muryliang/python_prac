import pymysql
from pymysql.err import InternalError #error when connect
from pymysql.err import ProgrammingError #error when execute 
from pymysql.err import DataError #error when data not fit type
import os
import pickle
import time
import sys

user = "root"
passwd = "123456"
host = "127.0.0.1"
db = "fishdb"
twtbl = "googlefishtable"

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

def get_or_create_db(host="127.0.0.1", user="root", passwd="123456", db="", use_unicode=True, charset="utf8"):
    try:
        connection = pymysql.connect(host=host, user=user, passwd=passwd, db=db, use_unicode=use_unicode, charset = charset)
        cur = connection.cursor()
        cur.execute("use {0}".format(db))
        print ("got database")
    except InternalError as e:
        print("db {0} not exist, create one".format(db))
        connection = pymysql.connect(host=host, user=user, passwd=passwd)
        cur = connection.cursor()
        cur.execute("create database {0} character set utf8".format(db))
        cur.execute("use {0}".format(db))
        connection.commit()
    return connection, cur

def create_twtable_if_needed(cursor, table):
    try:
        cursor.execute("desc {0}".format(table))
    except ProgrammingError as e:
        print ("table %s not exist, create one"%(table))
        ret = cursor.execute("create table {0} (id int not null auto_increment, \
                            engname varchar(50) not null, height int not null ,\
                            width int not null , imgsavename varchar(50) not null, \
                            fromurl varchar(1024) not null, objurl varchar(1024) not null, \
                            image longblob, primary key(id)) charset=utf8 ;".format(table))


def record_info(conn, cur, table):
    insert_str = "insert into {0} (engname, height, width, imgsavename, fromurl, objurl, image) \
            values (%s,%s,%s,%s,%s,%s,%s);"
    basedir = "/mnt/sdb1/google/fishgoogle/"
    meta = load_from_pickle("/mnt/sdb1/google/fishgoogle/dumpfish.dat")
    for key in meta.keys():
#        key = 'Chaetodon gentheri'
        curbasedir = os.path.join(basedir, key.replace(" ", "_"))
        print ("we have %d pictures for %s"%(len(meta[key]), key))
        urllist = load_exist(cur, key, table)
        print (urllist)
        args = list()
        starttime = time.time()
        for pic in meta[key]:
            info = meta[key][pic]
            if info['imgsavename'] in urllist:
                print ("url %s already inserted, skip" %(info['imgsavename']))
                continue
            picpath = os.path.join(curbasedir, info['imgsavename'])
            if os.path.exists(picpath):
                with open(picpath, "rb") as f:
                    imgdata = f.read()
                args.append( (info['name'], info['height'], info['width'],
                        info['imgsavename'], info['fromUrl'], info['imgurl'], imgdata))
#                cur.execute(insert_str.format(table), (info['name'], info['height'], info['width'],
#                            info['imgsavename'], info['fromUrl'], info['imgurl'], imgdata))
        cur.executemany(insert_str.format(table), args)
        conn.commit()
        endtime = time.time()
        print ("cost time:",endtime - starttime)
#        print ("only do one test")
#        break
    print ("done recoding")

def load_from_pickle(fname):
    with open(fname, "rb") as f:
        dic = pickle.load(f)
    return dic

def load_exist(cur, search, table):
    select_str = "select imgsavename from {0} where engname = %s"
    ret = cur.execute(select_str.format(table), (search,))
    return set(x[0] for x in cur)

#daemonize
#set outputfile
dir_prefix = "/home/jztec/python/logs"
stdoutfiletemplate = os.path.join(dir_prefix, "googlesql.log")
outfile = stdoutfiletemplate + "-" + time.strftime("%Y%m%d-%H%M%S")
open(outfile, "w").close()

#daemon your process
daemonize(stdout= outfile, stderr= outfile)

conn, cur = get_or_create_db(host, user, passwd, db)
create_twtable_if_needed(cur, twtbl)
try:
    record_info(conn, cur, twtbl)
finally:
    print ("start close database")
    conn.commit()
    cur.close()
    conn.close()
    print ("database closed")



