import tensorflow as tf

datadir = "/tmp/model/model.ckpt"
x = tf.Variable(tf.constant(1.0, shape=[1]), name="11" )
y = tf.Variable(tf.constant(2.0, shape=[1]), name ="22")

result = x + y
#saver = tf.train.Saver({"x1":x,"x2":y})
saver = tf.train.Saver({"Variable":x, "Variable_1":y})

with tf.Session() as sess:
    saver.restore(sess, datadir)
    print sess.run(result)
