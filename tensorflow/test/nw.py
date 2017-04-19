import tensorflow as tf
from numpy.random import RandomState

batch_size = 8
w1 = tf.Variable(tf.random_normal([2,3], stddev=1, seed = 1))
w2 = tf.Variable(tf.random_normal([3,1], stddev=1, seed = 1))

x = tf.placeholder(tf.float32, shape=(None, 2), name = "x-input")
y_ = tf.placeholder(tf.float32, shape=(None, 1), name = "y-input")

a = tf.matmul(x, w1)
y = tf.matmul(a, w2)
global_step = tf.Variable(0)

cross_entropy = -tf.reduce_mean(y_*tf.log(tf.clip_by_value(y, 1e-10, 1)))
learn_rate = tf.train.exponential_decay(0.1, global_step, 128/8, 0.96, staircase=True)
train_step = tf.train.AdamOptimizer(learn_rate).minimize(cross_entropy, global_step = global_step)

rdm = RandomState(1)
datasize = 128
X = rdm.rand(datasize, 2)
Y = [[int(x1+x2 < 1)] for (x1,x2) in X ]

with tf.Session() as sess:
    init_op = tf.initialize_all_variables()
    sess.run(init_op)
    print sess.run(w1)
    print sess.run(w2)

    STEP = 5000
    for i in range(STEP):
        start = (i * batch_size)% datasize
        end = min(start + batch_size, datasize)
        sess.run(train_step, feed_dict = {x:X[start:end], y_:Y[start:end]})

        if i % 1000 == 0:
            total_cross_entropy = sess.run(cross_entropy, feed_dict = {x:X[start:end], y_:Y[start:end]})
            print "after %d training steps, corss entropy is %g"%(i, total_cross_entropy)
            print sess.run(w1)
            print sess.run(w2)
