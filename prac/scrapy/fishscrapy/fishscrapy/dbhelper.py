import pymysql
from pymysql.err import InternalError, ProgrammingError

def create_db_if_needed(host="127.0.0.1", user="root", passwd="123456", db="", use_unicode=True, charset="utf8"):
    try:
        connection = pymysql.connect(host=host, user=user, passwd=passwd, db=db, use_unicode=use_unicode, charset = charset)
    except InternalError as e:
        print("db {0} not exist, create one".format(db))
        connection = pymysql.connect(host=host, user=user, passwd=passwd)
        cur = connection.cursor()
        cur.execute("create database {0} character set utf8".format(db))
        cur.execute("use {0}".format(db))
        connection.commit()
    return connection, cur

def create_table_if_needed(cursor, table):
    try:
        cursor.execute("desc {0}".format(table))
    except ProgrammingError as e:
        print ("table %s not exist, create one"%(table))
        ret = cursor.execute("create table {0} (picid bigint not null auto_increment, \
                            Spidername varchar(64) default null, \
                            Spiderinfo varchar(256) default null, \
                            fromURL varchar(2048) default null, \
                            objURL varchar(2048) default null, \
                            saveURL varchar(225) default null unique, \
                            thumbURL varchar(512) default null, \
                            width int(11) default null, \
                            height int(11) default null, \
                            size int(11) default null, \
                            type varchar(32) default null, \
                            name varchar(2048)  default null, \
                            keyword varchar(512) default null, \
                            classification varchar(512) default null, \
                            info varchar(8192) default null, \
                            gettime int(11) not null, \
                            primary key(picid)) charset=utf8; ".format(table))

def closedb(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

