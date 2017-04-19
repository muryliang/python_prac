import tensorflow as tf

datadir = "/tmp/model/model.ckpt"
x = tf.Variable(tf.constant(1.0, shape=[1]))
y = tf.Variable(tf.constant(2.0, shape=[1]))

result = x + y
saver = tf.train.Saver([x])

with tf.Session() as sess:
#    init_op = tf.initialize_all_variables()
#    sess.run(init_op)
#    print sess.run(result)
#    saver.save(sess, datadir)
    saver.restore(sess, datadir)
    print sess.run(x)
