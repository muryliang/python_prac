import pymysql
from pymysql.err import InternalError #error when connect
from pymysql.err import ProgrammingError #error when execute 
import os
import pickle
import math

user = "root"
passwd = "123456"
host = "127.0.0.1"
db = "fishdb"
twtbl = "twfishtable"

def get_or_create_db(host="127.0.0.1", user="root", passwd="123456", db="", use_unicode=True, charset="utf8"):
    try:
        connection = pymysql.connect(host=host, user=user, passwd=passwd, db=db, use_unicode=use_unicode, charset = charset)
        cur = connection.cursor()
        cur.execute("use {0}".format(db))
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
                            engname varchar(50) not null, chiname varchar(50) not null, \
                            scientific_name varchar(50) not null, objurl varchar(255) not null, \
                            image mediumblob, primary key(id)) charset=utf8 ;".format(table))


def record_info(conn, cur, table):
    insert_str = "insert into {0} (engname, chiname, scientific_name, objurl, image) \
            values (%s,%s,%s,%s,%s);"
    basedir = "/home/jztec/fish"
    meta = load_from_pickle("/home/jztec/fish/fishmeta.dat")
    for key in meta.keys():
        curbasedir = os.path.join(basedir, key.replace(" ", "_"))
        print ("we have %d pictures for %s"%(len(meta[key]['pictures']), key))
        urllist = load_exist(cur, key, table)
        for pic in meta[key]['pictures']:
            if pic in urllist:
                print ("url %s already inserted, skip" %(pic))
                continue
            picpath = os.path.join(curbasedir, pic.split("/")[-1].replace(" ","_").replace("gif", "jpg"))
            if os.path.exists(picpath):
                with open(picpath, "rb") as f:
                    imgdata = f.read()
                #中文名可能是float('nan'),一般是字符串，所以强制转换
                cur.execute(insert_str.format(table), (meta[key]['name'], str(meta[key]['中文名']), meta[key]['valid name'], pic, imgdata))
        conn.commit()
#        print ("only do one test")
#        break
    print ("done recoding")

def load_from_pickle(fname):
    twpickle = "/home/jztec/fish/fishmeta.dat"
    with open(twpickle, "rb") as f:
        dic = pickle.load(f)
    return dic

def load_exist(cur, search, table):
    select_str = "select objurl from {0} where engname = %s"
    ret = cur.execute(select_str.format(table), (search,))
    return set(x[0] for x in cur)

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



