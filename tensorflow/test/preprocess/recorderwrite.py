import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import os

data_dir = "/tmp/mnist_data"
#generate number feature
def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

#generate string feature
def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

mnist = input_data.read_data_sets(
        data_dir, dtype = tf.uint8, one_hot = True)
images = mnist.train.images
labels = mnist.train.labels
pixels = images.shape[1]
num_examples = mnist.train.num_examples

filename = "/tmp/tfrecorder/recorder"
if not os.path.exists("/tmp/tfrecorder"):
    os.makedirs("/tmp/tfrecorder")
writer = tf.python_io.TFRecordWriter(filename)
for index in range(num_examples):
    image_raw = images[index].tostring()
    example = tf.train.Example(features=tf.train.Features(feature={
        'pixels': _int64_feature(pixels),
        'label': _int64_feature(np.argmax(labels[index])),
        'iamge_raw': _bytes_feature(image_raw)}))
    writer.write(example.SerializeToString())
writer.close()
