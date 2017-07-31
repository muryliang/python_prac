from keras.preprocessing.image import ImageDataGenerator
from keras.applications.inception_v3 import InceptionV3, decode_predictions, preprocess_input
from keras.layers import Input
import pickle
import os

# in a while loop
## make symlink dir for flowdirectory
origname = getdir()
basedir = os.path.join('/home/sora', str(os.getpid()))
if not os.path.exists(basedir):
    os.makedirs(basedir)
picdir = os.path.join(basedir, origname.split('/')[-1])
os.symlink(origname, picdir)

batch_size=12
datagen = ImageDataGenerator()
test_generator = datagen.flow_from_directory(
        basedir,
        target_size=(224,224),
        batch_size=batch_size,
        shuffle=False)
filelist = test_generator.filenames

## below three can be put out of loop
input_tensor = Input(shape=(224,224,3))
input_tensor = preprocess_input(input_tensor)
model = InceptionV3(input_tensor=input_tensor, weights='imagenet', include_top=True)
## 
preds = model.predict_generator(test_generator, (test_generator.samples + batch_size -1)//batch_size)

## can be stored into mysql
assert len(preds) == len(filelist)
with open("/tmp/imgsave.dat", "wb") as f:
    pickle.dump(list(zip(preds, filelist)), f)
#print("Predicted: ") 
reslist = decode_predictions(preds, top=2)
for name, rate in zip(filelist, reslist):
    name = name.split('/')[-1]
    name = os.path.join('/'.join(origname.split('/')[-3:-1]), name)
    ## mysql operation
    # use update method of mysql to update the true false of that picture whether fish, selete with name above
    # both save that flag and the top 5

os.remove(picdir)
## mark in bloomfilter that the name_spider has been searched
#while loop end
