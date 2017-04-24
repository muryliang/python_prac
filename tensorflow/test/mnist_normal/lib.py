import tensorflow as tf

inputnode = 784
outputnode = 10
layernode = 500

def get_weight(shape, regular):
    weights = tf.get_variable("weights", shape, 
            initializer = tf.truncated_normal_initializer(stddev = 0.1))
    if regular != None:
        tf.add_to_collection("losses", regular(weights))
    return weights

def inference(input_tensor, regular):
    with tf.variable_scope("weight1"):
        weights = get_weight([inputnode, layernode], regular)
        biases = tf.get_variable("biases", [layernode], initializer = tf.constant_initializer(0.0))
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights) + biases)

    with tf.variable_scope("weight2"):
        weights = get_weight([layernode, outputnode], regular)
        biases = tf.get_variable("biases", [outputnode], initializer = tf.constant_initializer(0.0))
        layer2 = tf.matmul(layer1, weights) + biases
    return layer2

