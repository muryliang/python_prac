import tensorflow as tf
w1 = tf.Variable(tf.random_normal([2,3], stddev = 1), name = "w1")
w2 = tf.Variable(tf.random_normal([2,2], stddev = 1), name = "w2")

w5 = tf.get_variable("v", [1])
with tf.variable_scope("foo"):
    w3 = tf.get_variable("v", [1])
with tf.variable_scope("", reuse=True):
    w4 = tf.get_variable("foo/v", [1])
    print w3 == w4
with tf.variable_scope("", reuse=True):
    w6 = tf.get_variable("v", [1])
#tf.assign(w1, w2)
#ass = tf.assign(w1, w2, validate_shape=False)


with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    print sess.run([w3,w4,w5])
