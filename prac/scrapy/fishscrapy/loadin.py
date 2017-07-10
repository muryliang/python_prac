import pickle
import redis

class redisConn():
    host='127.0.0.1'
    port=6379
    csvfile = "/home/sora/fishsorts.dat"
    
    def __init__(self, lname='fish'):
        """initialize with list's name
        """
        self.lname = lname

    def getConnPool(self):
        """get connection pool from redis
        """
        self.pool = redis.ConnectionPool(host=self.host, port=self.port)

    def load_name(self, sort='engname'):
        """load dictionary from picklefile
            sort: chiname or engname
        """
        with open(self.csvfile, "rb") as f:
            fishnames = pickle.load(f)
            self.names = fishnames[sort]

    def insertRedis(self):
        """insert names into redis
        """
        r = redis.Redis(connection_pool=self.pool)
        for name in self.names:
            r.lpush(self.lname, name)

            
conn = redisConn('baidufish')
conn.load_name('chiname')
conn.getConnPool()
conn.insertRedis()
