import tensorflow as tf
from numpy.random import RandomState

X = tf.placeholder(tf.float32, shape=(None, 2), name = "x-input")
Y = tf.placeholder(tf.float32, shape=(None, 1), name = "y-input")

def get_weight(in_dim, out_dim, lam):
    w = tf.Variable(tf.random_normal([in_dim, out_dim], lam, seed = 1))
    tf.add_to_collection("loss", tf.contrib.layers.l2_regularizer(lam)(w))
    return w

cur_layer = X
dimentional = [2, 10, 10, 8, 1]
in_dim = dimentional[0]
for i in range(1, len(dimentional)):
    out_dim = dimentional[i]
    w = get_weight(in_dim, out_dim, 0.001)
    bias = tf.Variable(tf.constant(0.1, shape=[out_dim]))
    cur_layer = tf.nn.relu(tf.matmul(cur_layer, w) + bias)
    in_dim = out_dim

mes_loss = tf.reduce_mean(tf.square(Y - cur_layer))
tf.add_to_collection("loss", mes_loss)

loss = tf.add_n(tf.get_collection("loss"))

global_step = tf.Variable(0)
learn_rate = tf.train.exponential_decay(0.03, global_step, 128 / 8, 0.95, staircase=True)
train = tf.train.AdamOptimizer(learn_rate).minimize(loss, global_step = global_step)

STEP = 10000
datasize = 128
batch_size = 8
rdm = RandomState(1)
x_input = rdm.rand(datasize, 2)
y_input = [[x1 + y1 + rdm.rand()/10.0 - 0.05] for (x1, y1) in x_input]

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    print sess.run(tf.trainable_variables())
    for i in range(STEP):
        start = i * batch_size % datasize
        end = min(start + batch_size, datasize)
        sess.run(train, feed_dict = {X: x_input[start:end], Y: y_input[start:end]})
        if i % 1000 == 0:
            print "begin loss"
            for i in tf.get_collection("loss"):
                print sess.run(i,  feed_dict = {X: x_input[start:end], Y: y_input[start:end]})
            print "end loss"
            print sess.run(loss, feed_dict = {X: x_input[start:end], Y: y_input[start:end]})
    

