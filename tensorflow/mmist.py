#-*- coding: utf-8 -*-
import input_data
import tensorflow as tf
mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)

x = tf.placeholder(tf.float32, [None, 784]) #一个占位符，第一维度可以无线延伸
W = tf.Variable(tf.zeros([784, 10]))
#在这里面，这个Ｗ就是一个，筛子，每一列代表对应数字的筛子，每次都是一个７４８像素的ｘ的输入
#和１０列这样的筛子得出１０个结果，可以理解为１０个向量的相似程度，越相似，就越代表几率高，
#这个几率由ｓｏｆｔｍａｘ来整合得到,最后拿几率最高的出去比较，代表就是这个数，求概率
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(x, W) + b)
y_ = tf.placeholder("float", [None, 10])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict = {x:batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print sess.run(accuracy, feed_dict = {x: mnist.test.images, y_ : mnist.test.labels})
