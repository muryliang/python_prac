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

    img_data = tf.image.convert_image_dtype(img_data, dtype=tf.float32)
    resized = tf.image.resize_images(img_data, 768,1024, method=2)
    resized = tf.image.convert_image_dtype(resized, dtype=tf.uint8)
    encoded_image = tf.image.encode_jpeg(resized)
    with tf.gfile.GFile(dest_file, "wb") as f:
        f.write(encoded_image.eval())
