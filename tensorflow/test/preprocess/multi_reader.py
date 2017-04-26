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

with tf.Session() as sess:
    tf.initialize_all_variables().run()
    print sess.run(files)

    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    for i in range(8):
        print sess.run([features['i'], features['j']])
    coord.request_stop()
    coord.join(threads)
