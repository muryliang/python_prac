import time
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import lib
import train
import numpy as np

eval_interval_sec = 10

def evaluate(mnist):
    val_size = mnist.validation.num_examples
    with tf.Graph().as_default() as g:
        x = tf.placeholder(tf.float32, [val_size, lib.image_size, lib.image_size, lib.num_channels], name='x-input')
        y_ = tf.placeholder(tf.float32, [None, lib.outputnode], name='y-input')
        reshaped_val_x = np.reshape(mnist.validation.images, (val_size, lib.image_size, lib.image_size, lib.num_channels))
        validate_feed = {x:reshaped_val_x, y_:mnist.validation.labels}
        y = lib.inference(x, None, None)
        correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        variable_averages = tf.train.ExponentialMovingAverage(
                train.moving_averate_decay)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)

        while True:
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(
                        train.model_save_path)
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    global_step = ckpt.model_checkpoint_path\
                            .split('/')[-1].split('-')[-1]
                    accuracy_score = sess.run(accuracy, feed_dict=validate_feed)
                    print "after %s steps, accuracy is %g"%(global_step, accuracy_score)
                else:
                    print "no checkpoint file found"
                    return
                time.sleep(eval_interval_sec)
def main(argv=None):
    mnist = input_data.read_data_sets(train.data_dir, one_hot = True)
    evaluate(mnist)

if __name__ == "__main__":
    tf.app.run()
