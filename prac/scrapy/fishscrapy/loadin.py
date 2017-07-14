import pickle
import redis
from six.moves.urllib.parse import urlencode

#base class
class redisConn():
    """read class name from file,these data are
       preprocessed from
       /home/sora/fishsorts(2).dat
    """
    host='127.0.0.1'
    port=6379
    engfile = "/home/sora/twengname_processed.dat"
    chifile = "/home/sora/twchiname_processed.dat"
    
    def __init__(self, lname='fish', base_url="", lang='engname'):
        """initialize with list's name and base_url
        """
        self.lname = lname
        self.base_url = base_url
        self.lang = lang

    def getConnPool(self):
        """get connection pool from redis
        """
        self.pool = redis.ConnectionPool(host=self.host, port=self.port)

    def load_name(self, sort='engname'):
        """load dictionary from picklefile
            sort: chiname or engname
        """
        if sort == 'engname':
            with open(self.engfile, "rb") as f:
                self.names = pickle.load(f)
        else:
            with open(self.chifile, "rb") as f:
                self.names = pickle.load(f)

    def insertRedis(self):
        """insert names into redis
        """
        pass

class baiduConn(redisConn):

    def insertRedis(self):
        """insert names into redis
        """
        self.load_name(self.lang)
        self.getConnPool()
        r = redis.Redis(connection_pool=self.pool)
        for name in self.names[:5]:
            for page in range(0,480,60):
                r.rpush(self.lname, self.base_url.format(name,str(page)))

class googleConn(redisConn):

    def insertRedis(self):
        """insert names into redis
        """
        self.load_name(self.lang)
        self.getConnPool()
        r = redis.Redis(connection_pool=self.pool)
        for name in self.names[:5]:
            for page in range(0,12):
                params = dict (q=name, ijn=page, start=page*100, tbm='isch')
                url = self.base_url + urlencode(params)
                r.rpush(self.lname, url)

class twConn(redisConn):

    def insertRedis(self):
        """insert names into redis
        """
        self.load_name(self.lang)
        self.getConnPool()
        r = redis.Redis(connection_pool=self.pool)
        for name in self.names[:20]:
            url = self.base_url + "+".join(name.split(" "))
            r.rpush(self.lname, url)

class algaebaseConn(redisConn):

    def insertRedis(self):
        """insert names into redis
           algaebase just push name , because requests are post
        """
        self.load_name(self.lang)
        self.getConnPool()
        r = redis.Redis(connection_pool=self.pool)
#        self.names = ['Ascophyllum nodosum',]
        lst = self.names[:18]
        lst.extend(['Porphyra linearis', 'Palmaria palmata'])
        for name in lst:
            r.rpush(self.lname, self.base_url + "," + name)

class fishbaseConn(redisConn):

    def insertRedis(self):
        """insert names into redis
           algaebase just push name , because requests are post
        """
        self.load_name(self.lang)
        self.getConnPool()
        r = redis.Redis(connection_pool=self.pool)
        for name in self.names[:20]:
            lst = name.split(" ")
            r.rpush(self.lname, self.base_url.format(lst[0],lst[1]))


baidu_base_url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word={0}&cg=girl&pn={1}&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
google_base_url = 'https://www.google.com/search?'
tw_base_url = 'http://fishdb.sinica.edu.tw/chi/synonyms_list.php?id=&pz=25&page=0&R1=&key='
algaebase_base_url = 'http://www.algaebase.org/search/images'
fishbase_base_url = 'http://fishbase.sinica.edu.tw/Summary/SpeciesSummary.php?genusname={0}&speciesname={1}&lang=Chinese'

#this is for baidu            
conn_baidu = baiduConn('baiduurl', baidu_base_url, 'chiname')
conn_baidu.insertRedis()

#this for google
conn_google = googleConn('googleurl', google_base_url, 'engname')
conn_google.insertRedis()

#this for taiwan
conn_tw = twConn('twurl', tw_base_url, 'engname')
conn_tw.insertRedis()

#this for algaebase
conn_algaebase = algaebaseConn('algaebaseurl', algaebase_base_url, 'engname')
conn_algaebase.insertRedis()

#this for fishbase
conn_fishbase = fishbaseConn('fishbaseurl', fishbase_base_url, 'engname')
conn_fishbase.insertRedis()
