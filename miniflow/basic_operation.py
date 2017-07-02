# -*- coding: utf-8 -*-
import miniflow.miniflow as tf

sess = tf.Session()

hello = tf.constant("Hello, MiniFlow!")
print(sess.run(hello))

a = tf.constant(32.0)
b = tf.constant(10.0)

c = a + b
print(sess.run(c))

c = a - b
print(sess.run(c))

c = a * b
print(sess.run(c))

c = a / b
print(sess.run(c))