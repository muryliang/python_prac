import tensorflow as tf
import time

files = tf.train.match_filenames_once("/tmp/data.tfrecord-*")
filename_queue = tf.train.string_input_producer(files, shuffle=False)
reader = tf.TFRecordReader()

_, serialized_example = reader.read(filename_queue)
features = tf.parse_single_example(
        serialized_example,
        features={
            'i':tf.FixedLenFeature([], tf.int64),
            'j':tf.FixedLenFeature([], tf.int64),
        })

example, label = features['i'], features['j']

batch_size = 3

capacity = 1000 + 3 * batch_size
example_batch, label_batch = tf.train.batch(
        [example, label], batch_size=batch_size, capacity= capacity)
with tf.Session() as sess:
    tf.initialize_all_variables().run()
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess = sess, coord = coord)
    for i in range(2):
        curexp, curlab = sess.run([example_batch, label_batch])
        print curexp, curlab
    coord.request_stop()
    coord.join(threads)

with tf.Session() as sess:
    tf.initialize_all_variables().run()
    print sess.run(files)

    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    for i in range(8):
        print sess.run([features['i'], features['j']])
    coord.request_stop()
    coord.join(threads)
