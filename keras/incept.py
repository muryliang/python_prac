from keras.preprocessing.image import ImageDataGenerator
from keras.applications.inception_v3 import InceptionV3, decode_predictions, preprocess_input
from keras.layers import Input, Lambda
import pickle
import os
import sys
import pymysql
import redis

def updatedb(cur, conn, saveurl, ratelist, tablename, classlist):
    """update mysql entry saveurl the rate list and boolean of fish"""

    flag = 1
    for result in ratelist:
        if result[1] in classlist:
            flag = 2
            break

    tablename = 'algaebasemeta'
    saveurl = 'imgdata/hehe/10a1c30f059b1e5250cebb2a5dd7656a5a4f17f4.jpg'
    cur.execute("update {0} set isfish=%s, top5rate=%s where saveURL=%s;".format(tablename),
        (str(flag), str(ratelist), saveurl))
    conn.commit()

# global settings
dirqueue = 'classQueue'
redishost = '10.0.0.121'
batch_size=32
tmpdir = '/home/jztec/picdir'
existfile = 'results.dat'
basedir = os.path.join(tmpdir, str(os.getpid()))
if not os.path.exists(basedir):
    os.makedirs(basedir)

# mysql conn: store result
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='fishdb', use_unicode=True, charset='utf8')
cur = conn.cursor()
# redis conn: get directory
r = redis.Redis(host=redishost, port=6379)

classlist = set("tench", "goldfish", "great_white_shark", "tiger_shark", "hammerhead", "electric_ray", 
        "stingray", "loggerhead", "leatherback_turtle", "mud_turtle", "terrapin", "box_turtle", "African_crocodile",
        "American_alligator", "jellyfish", "sea_anemone", "brain_coral", "flatworm", "nematode", "conch",
        "snail", "slug", "sea_slug", "chiton", "chambered_nautilus", "Dungeness_crab", "rock_crab", "fiddler_crab", 
        "king_crab", "American_lobster", "spiny_lobster", "crayfish", "hermit_crab", "isopod", "king_penguin", 
        "grey_whale", "killer_whale", "dugong", "sea_lion", "starfish", "sea_urchin", "sea_cucumber", "barracouta",
        "eel", "coho", "rock_beauty", "anemone_fish", "sturgeon", "gar", "lionfish", "puffer") 

## create model
input_tensor = Input((299,299,3))
x = input_tensor
x = Lambda(preprocess_input)(x)
model = InceptionV3(input_tensor=x, weights='imagenet', include_top=True)

# in a while loop
while True:
    origname = r.lpop(dirqueue)
    if origname is None:
        break
    origname = origname.decode('utf8') # get from redis

    datasavefile = os.path.join(origname, existfile) # check if already analized
    if os.path.exists(datasavefile):
        print ("already downloaded %s"%(origname))
        continue

    ## make symlink dir for flowdirectory
    picdir = os.path.join(basedir, origname.split('/')[-1])
    os.symlink(origname, picdir)

    # generate from pictures in file
    datagen = ImageDataGenerator()
    test_generator = datagen.flow_from_directory(
            basedir,
            target_size=(299,299),
            batch_size=batch_size,
            shuffle=False)
    filelist = test_generator.filenames

    preds = model.predict_generator(test_generator, (test_generator.samples + batch_size -1)//batch_size)
    assert len(preds) == len(filelist)

    reslist = decode_predictions(preds, top=5)
    for name, rate in zip(filelist, reslist):
        name = name.split('/')[-1]
        name = os.path.join('/'.join(origname.split('/')[-3:-1]), name)
        spider = origname.split('/')[-3]
        updatedb(cur, conn, name, rate, spider + "meta", classlist) # mysql update statement

    # used as a check whether already processed
    with open(datasavefile, "wb") as f:
        pickle.dump(list(zip(preds, filelist)), f)

    os.remove(picdir)
    #while loop end
conn.commit()
cur.close()
conn.close()
