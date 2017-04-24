import  tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os
import lib
import numpy as np


batch_size = 100
learning_rate_base = 0.01 #this should be small when using convolutional
learn_decay_rate = 0.99
regular_rate = 0.0001
num_train_step = 30000
moving_averate_decay = 0.99
model_save_path = "/tmp/model"
model_name = "model_lenet.ckpt"
data_dir = "/tmp/data"

def train(mnist):
    x = tf.placeholder(tf.float32, [batch_size, lib.image_size, lib.image_size, lib.num_channels], name='x-input')
    y_ = tf.placeholder(tf.float32, [batch_size, lib.outputnode], name='y-input')

    regular = tf.contrib.layers.l2_regularizer(regular_rate)
    y = lib.inference(x, True, regular)

    global_step = tf.Variable(0, trainable=False)
    variable_averages = tf.train.ExponentialMovingAverage(
            moving_averate_decay, global_step)
    variable_op = variable_averages.apply(tf.trainable_variables())
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
            y, tf.argmax(y_, 1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    loss = cross_entropy_mean + tf.add_n(tf.get_collection("losses"))
    learning_rate = tf.train.exponential_decay(
            learning_rate_base, global_step, mnist.train.num_examples / batch_size,
            learn_decay_rate)
    train_step = tf.train.GradientDescentOptimizer(learning_rate)\
            .minimize(loss, global_step=global_step)
    with tf.control_dependencies([train_step, variable_op]):
        train_op = tf.no_op(name = 'train')
    
    saver = tf.train.Saver()
    with tf.Session() as sess:
        tf.initialize_all_variables().run()
        for i in range(num_train_step):
            xs, ys = mnist.train.next_batch(batch_size)
            reshaped_xs = np.reshape(xs, (batch_size,
                                        lib.image_size,
                                        lib.image_size,lib.num_channels))
            _, loss_value, step = sess.run([train_op, loss, global_step],
                                        feed_dict = {x:reshaped_xs, y_:ys})
            if i % 1000 == 0:
                print "after %d steps, loss on training batch is %g." %(step, loss_value)
                saver.save(sess, os.path.join(model_save_path, model_name), global_step = global_step)
def main(argv=None):
    mnist = input_data.read_data_sets(data_dir, one_hot = True)
    train(mnist)

if __name__ == "__main__":
    tf.app.run()
