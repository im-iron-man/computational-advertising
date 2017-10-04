import tensorflow as tf

W = tf.Variable([[1, 2, 3], [3, 4, 5]], dtype=tf.float32, name='weights')
b = tf.Variable([[1, 2, 3]], dtype=tf.float32, name='biases')

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.globals_variables_initializer())
    save_path = saver.save(sess, 'my_net/save_net.ckpt')
    print('Save to path: ', save_path)