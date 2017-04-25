import matplotlib.pyplot as plt
import tensorflow as tf

src_file = "/home/sora/Downloads/tensorflow_data/flower_photos/daisy/3640845041_80a92c4205_n.jpg"
dest_file = "/tmp/flower.jpg"

image_data_raw = tf.gfile.FastGFile(src_file, 'r').read()

with tf.Session() as sess:
    img_data = tf.image.decode_jpeg(image_data_raw)

    #print img_data.eval()
    plt.imshow(img_data.eval())
#    plt.show()

    boxes = tf.constant([[[0.05,0.05,0.9,0.7], [0.35,0.47,0.5,0.56]]])
    begin, size, bbox_for_draw = tf.image.sample_distorted_bounding_box(
            tf.shape(img_data), bounding_boxes = boxes)
    batched = tf.expand_dims(tf.image.convert_image_dtype(img_data, tf.float32), 0)
    image_with_box = tf.image.draw_bounding_boxes(batched, bbox_for_draw)
    plt.imshow(tf.image.convert_image_dtype(image_with_box, dtype=tf.uint8))
    plt.show()
    distorted_image = tf.slice(img_data, begin, size)
    image_with_box = tf.image.convert_image_dtype(distorted_image, dtype=tf.uint8)
    encoded_image = tf.image.encode_jpeg(image_with_box)
    with tf.gfile.GFile(dest_file, "wb") as f:
        f.write(encoded_image.eval())
#with tf.Session() as sess:         
#
#    boxes = tf.constant([[[0.05, 0.05, 0.9, 0.7], [0.35, 0.47, 0.5, 0.56]]])
#
#    begin, size, bbox_for_draw = tf.image.sample_distorted_bounding_box(
#        tf.shape(img_data), bounding_boxes=boxes)
#
#
#    batched = tf.expand_dims(tf.image.convert_image_dtype(img_data, tf.float32), 0) 
#    image_with_box = tf.image.draw_bounding_boxes(batched, bbox_for_draw)
#    
#    distorted_image = tf.slice(img_data, begin, size)
#    plt.imshow(distorted_image.eval())
#    plt.show()
