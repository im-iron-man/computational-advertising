# -*- coding: utf-8 -*-
import math
import random

class AnnealingEpsilonGreedy(object):

    def __init__(self, n_arms):
        self.counts = [0 for _ in range(n_arms)]
        self.values = [0.0 for _ in range(n_arms)]

    def pull(self):
        t = sum(self.counts) + 1
        epsilon = 1 / math.log(t + 0.0000001)
        if random.random() > epsilon:
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