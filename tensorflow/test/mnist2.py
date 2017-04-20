import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

datadir = "/tmp/MNIST"
input_node = 784
output_node = 10
layer_node = 500
moving_rate = 0.99
regularization_rate = 0.0001
base_learn = 0.8
batch_size = 100
decay_rate = 0.99
training_step = 30000

#use neural network to compute results
def predict(xdata, cls_model, weight1, bias1, weight2, bias2):
    if cls_model == None: #no slide
        y1 = tf.nn.relu(tf.matmul(xdata, weight1) + bias1)
        y2 = tf.matmul(y1, weight2) + bias2
    else:
        y1 = tf.nn.relu(tf.matmul(xdata, cls_model.average(weight1)) + cls_model.average(bias1))
        y2 = tf.matmul(y1, cls_model.average(weight2)) + cls_model.average(bias2)
    return y2

def train(mnist):
    w1 = tf.Variable(tf.truncated_normal([input_node, layer_node], stddev = 0.1))
    b1 = tf.Variable(tf.constant(0.1, shape = [layer_node]))
    w2 = tf.Variable(tf.truncated_normal([layer_node, output_node], stddev = 0.1))
    b2 = tf.Variable(tf.constant(0.1, shape = [output_node]))
    x = tf.placeholder(tf.float32, [None, input_node], name = "x-input")
    y_ = tf.placeholder(tf.float32, [None, output_node] , name = "y-input")

    y = predict(x, None, w2, b1, w2, b2) # get batch predict result

    global_step = tf.Variable(0, trainable=False)
    variable_average = tf.train.ExponentialMovingAverage(
            moving_rate, global_step)
    variable_average_op = variable_average.apply(tf.trainable_variables())

    average_y = predict(x, variable_average, w1, b1, w2, b2)

    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
            y, tf.argmax(y_, 1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)

    regularizer = tf.contrib.layers.l2_regularizer(regularization_rate)
    regularization = regularizer(w1) + regularizer(w2)

    loss = cross_entropy_mean + regularization

    learning_rate = tf.train.exponential_decay(
            base_learn, global_step, mnist.train.num_examples / batch_size, decay_rate, staircase=True)

    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step = global_step)

    with tf.control_dependencies([train_step, variable_average_op]):
        train_op = tf.no_op(name ='train')


    correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    with tf.Session() as sess:
        tf.initialize_all_variables().run()
        validate_feed = {x: mnist.validation.images, y_:mnist.validation.labels}
        test_feed = {x: mnist.test.images, y_:mnist.test.labels}

        for i in range(training_step):
            if i % 1000 == 0:
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)
                print "after %d steps, validate accuracy is %g"%(i, validate_acc)
            xs, ys = mnist.train.next_batch(batch_size)
            sess.run(train_op, feed_dict = {x:xs, y_:ys})

        test_acc = sess.run(accuracy, feed_dict = test_feed)
        print "after %d training steps, test accuracy using average model is %g"%(training_step, test_acc)

def main(argv = None):
    mnist = input_data.read_data_sets(datadir, one_hot = True)
    train(mnist)

if __name__ == "__main__":
    tf.app.run()
