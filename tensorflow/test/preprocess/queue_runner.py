import tensorflow as tf
import numpy as np
import sys

queue = tf.FIFOQueue(100, "float")
enqueue_op = queue.enqueue([tf.random_normal([1])])

qr = tf.train.QueueRunner(queue, [enqueue_op] * 3)
tf.train.add_queue_runner(qr)
out_tensor = queue.dequeue()

with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    for _ in range(int(sys.argv[1])):
        print sess.run(out_tensor)[0]
    coord.request_stop()
    coord.join(threads)
