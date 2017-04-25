import tensorflow as tf

reader = tf.TFRecordReader()
filename_queue = tf.train.string_input_producer(
        ["/tmp/tfrecorder/recorder"])
_, serialized_example = reader.read(filename_queue)
features = tf.parse_single_example(
        serialized_example,
        features = {
            'iamge_raw': tf.FixedLenFeature([], tf.string),
            'pixels': tf.FixedLenFeature([], tf.int64),
            'label': tf.FixedLenFeature([], tf.int64),
        })

images = tf.decode_raw(features['iamge_raw'], tf.uint8)
labels = tf.cast(features['label'], tf.int32)
pixels = tf.cast(features['pixels'], tf.int32)

sess = tf.Session()
coord = tf.train.Coordinator()
threads = tf.train.start_queue_runners(sess=sess, coord =coord)

for i in range(10):
    image, label, pixel = sess.run([images, labels, pixels])
    print image
    print label,
    print pixel
    print 
