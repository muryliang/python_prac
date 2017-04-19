import tensorflow as tf
from numpy.random import RandomState

x = tf.placeholder(tf.float32, shape=(None, 2), name = "x-input")
y_ = tf.placeholder(tf.float32, shape=(None, 1), name = "y-input")

w1 = tf.Variable(tf.random_normal([2,1], stddev=1, seed = 1))
y = tf.matmul(x, w1)

loss_more = 1
loss_less = 10
loss = tf.reduce_sum(tf.select(tf.greater(y, y_),
                                (y - y_)*loss_more,
                                (y_ - y)*loss_less))

train_step = tf.train.AdamOptimizer(0.001).minimize(loss)
rdm = RandomState(1)
batch_size = 8
datasize = 128
X = rdm.rand(datasize, 2)
Y = [[x1 + x2 + rdm.rand()/10.0 - 0.05] for (x1, x2) in X]

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    STEPS = 5000
    for i in range(STEPS):
        start = i*batch_size % datasize
        end = min(start + batch_size, datasize)
        sess.run(train_step,
                feed_dict = {x:X[start:end],y_:Y[start:end]})
        print sess.run(w1) 
