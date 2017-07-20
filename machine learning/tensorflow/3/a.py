# -*- coding: utf-8 -*-
import tensorflow as tf

state = tf.Variable(0, name='counter')
print(state)
print(state.name)
one = tf.constant(1)
print(one)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))