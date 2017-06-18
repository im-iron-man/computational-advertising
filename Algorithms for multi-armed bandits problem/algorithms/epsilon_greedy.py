# -*- coding: utf-8 -*-
import random

class EpsilonGreedy(object):

    def __init__(self, epsilon, n_arms):
        self.epsilon = epsilon
        self.counts = [0 for _ in range(n_arms)]
        self.values = [0.0 for _ in range(n_arms)]

    def pull(self):
        if random.random() > self.epsilon:
            m = max(self.values)
            return self.values.index(m)
        else:
            return random.randrange(len(self.values))

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        new_value = ((n-1) * value + reward) / n
        self.values[chosen_arm] = new_value