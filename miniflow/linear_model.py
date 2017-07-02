# -*- coding: utf-8 -*-
import miniflow.miniflow as tf

def linear_regression():
    epoch_number = 30
    learning_rate = 0.01
    train_features = [1.0, 2.0, 3.0, 4.0, 5.0]
    train_labels = [10.0, 20.0, 30.0, 40.0, 50.0]

    weights = tf.Variable(0.0)
    bias = tf.Variable(0.0)
    x = tf.placeholder(tf.float32)
    y = tf.placeholder(tf.float32)

    predict = weights * x + bias
    loss = tf.square(y - predict)
    sgd_optimizer =