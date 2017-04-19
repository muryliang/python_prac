import tensorflow as tf

datadir = "/tmp/model/model.ckpt"
x = tf.Variable(tf.constant(1.0, shape=[1]), name="other-v1")
y = tf.Variable(tf.constant(2.0, shape=[1]), name="other-v2")

result = x + y
saver = tf.train.Saver()

with tf.Session() as sess:
    saver.save(sess, datadir)
    print sess.run(result)
