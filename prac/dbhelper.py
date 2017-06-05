import pymysql
from pymysql.err import InternalError #error when connect
from pymysql.err import ProgrammingError #error when execute 
from pymysql.err import DataError #error when data not fit type
import os
import pickle
import time
import sys


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
        ret = cursor.execute( "CREATE TABLE `{0}` ( \
            `picid` bigint(20) NOT NULL AUTO_INCREMENT, \
            `Spidername` varchar(64) DEFAULT NULL, \
            `fromURL` varchar(512) DEFAULT NULL, \
            `objURL` varchar(2048) DEFAULT NULL, \
            `saveURL` varchar(512) DEFAULT NULL, \
            `width` int(11) DEFAULT NULL, \
            `height` int(11) DEFAULT NULL, \
            `size` int(11) DEFAULT NULL, \
            `type` varchar(32) DEFAULT NULL, \
            `name` varchar(256) DEFAULT NULL, \
            `keyword` varchar(512) DEFAULT NULL,  \
            `classification` varchar(512) DEFAULT NULL, \
            `info` varchar(8192) DEFAULT NULL, \
            `gettime` int(11) NOT NULL, \
            PRIMARY KEY (`picid`) \
        )  DEFAULT CHARSET=utf8;".format(table))

def insert_info_one(conn, cur, table, record, basedir):
    insert_str = "insert into {0} (Spidername, fromURL, objURL, saveURL, width, height, size, type, name, keyword, \
            classification, info, gettime) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,UNIX_TIMESTAMP());"
    key = record['name']
    print ("begin store ", key)
    curbasedir = os.path.join(basedir, key.replace(" ", "_"))
    args = list()
    info = record
    picpath = os.path.join(curbasedir, info['imgsavename'])
    if os.path.exists(picpath):
        param = (("googlespider",info['fromUrl'],info['imgurl'],info['imgsavename'],info['width'],info['height'],
            "0", "jpg", info['imgsavename'], info['name'], "", str(info['desc'])))
        cur.execute(insert_str.format(table), param)
#    cur.executemany(insert_str.format(table), args)
    conn.commit()


def load_exist(cur, search, table):
    select_str = "select saveURL, objURL from {0} where keyword = %s"
    ret = cur.execute(select_str.format(table), (search,))
    res = cur.fetchall()
    return set(x[0] for x in res), set(x[1] for x in res)

if __name__ == "__main__":
    user = "root"
    passwd = "123456"
    host = "127.0.0.1"
    db = "fishdb"
    twtbl = "googlefishtable"
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



