# -*- coding: utf-8 -*-
import math
import random

def _dot_operation(x, y):
    assert len(x) == len(y)
    return sum([x[i] * y[i] for i in range(len(x))])

class MonteCarloPolicyGradientAgent(object):

    def __init__(self, act_n, gamma=0.9, step=0.01):
        self.act_n = act_n
        self.gamma = gamma
        self.step = step
        self.theta = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.episode = []

    def _make_feature(self, state, action):
        return [state[0], state[1], state[2], state[3], action]

    def _pi(self, state, action):
        t1 = math.exp(_dot_operation(self._make_feature(state, action), self.theta))
        t2 = sum([math.exp(_dot_operation(self._make_feature(state, a), self.theta)) for a in range(self.act_n)])
        return t1 / t2

    def choose(self, state):
        probs = [self._pi(state, a) for a in range(self.act_n)]
        t = random.random()
        cum_prob = 0.0
        for i in range(self.act_n):
            cum_prob += probs[i]
            if cum_prob > t:
                return i
        return len(probs) - 1

    def store(self, state, action, reward):
        self.episode.append((state, action, reward))

    def learn(self):
        total_reward = 0
        for state, action, reward in reversed(self.episode):
            total_reward = reward + self.gamma * total_reward
            theta = [0.0] * len(self.theta)
            t1 = self._make_feature(state, action)
            t2 = [self._pi(state, a) for a in range(self.act_n)]
            t3 = [self._make_feature(state, a) for a in range(self.act_n)]
            for i in range(len(self.theta)):
                theta[i] = self.theta[i] + self.step * (t1[i] - _dot_operation(t2, [t[i] for t in t3])) * total_reward
            self.theta = theta
        self.episode = []