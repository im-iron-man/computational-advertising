import numpy as np
import pandas as pd
import tensorflow as tf

np.random.seed(1)
tf.set_random_seed(1)

def _add_layer(inputs, in_size, out_size, activation_function=None):
    weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    outputs = tf.matmul(inputs, weights) + biases
    return activation_function(outputs) if activation_function else outputs

class DeepQNetwork:

    def __init__(self, n_features, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        self.n_features = n_features
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self._build_network()
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())

    def _build_network(self):
        self.state_action = tf.placeholder(tf.float32, [None, self.n_features+1])
        self.q_target = tf.placeholder(tf.float32, [None, 1])
        layer1 = _add_layer(self.state_action, self.n_features+1, 10, activation_function=tf.nn.relu)
        self.q_predict = _add_layer(layer1, 10, 1)
        loss = tf.reduce_mean(tf.reduce_sum(tf.square(self.q_target - self.q_predict), reduction_indices=[1]))
        self.train = tf.train.GradientDescentOptimizer(self.lr).minimize(loss)

    def _make_features(self, s, a):
        return np.array([[s[0], s[1], a/4.0]])

    def choose_action(self, s):
        q_target = None
        if np.random.uniform() < self.epsilon:
            for action in range(4):
                t = self.sess.run(self.q_predict, feed_dict={self.state_action: self._make_features(s, action)})
                if q_target is None or q_target < t:
                    q_target, a = t, action
        else:
            a = np.random.randint(0, 4)
        return a

    def learn(self, s, a, r, s_):
        q_target = None
        for action in range(4):
            t = self.sess.run(self.q_predict, feed_dict={self.state_action: self._make_features(s_, action)})
            if q_target is None or q_target < t:
                q_target = t
        q_target = r + self.gamma * q_target
        self.sess.run(self.train, feed_dict={self.state_action: self._make_features(s, a), self.q_target: q_target})