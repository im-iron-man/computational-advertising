# -*- coding: utf-8 -*-
import miniflow.miniflow as tf

sess = tf.Session()

a = tf.placeholder(tf.float32)
b = tf.constant(32.0)
print(sess.run(a + b, feed_dict={a: 10}))
print(sess.run(a + b, feed_dict={a.name: 10}))