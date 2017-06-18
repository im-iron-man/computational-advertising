# -*- coding: utf-8 -*-
import math
import random

class Pursuit(object):

    def __init__(self, beta, n_arms):
        self.beta = beta
        self.counts = [0 for _ in range(n_arms)]
        self.values = [0.0 for _ in range(n_arms)]
        self.probs = [1.0/n_arms for _ in range(n_arms)]

    def pull(self):
        n_arms = len(self.counts)
        for arm in range(n_arms):
            if self.counts[arm] == 0:
                return arm
        m = max(self.probs)
        return self.probs.index(m)

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        new_value = ((n-1) * value + reward) / n
        self.values[chosen_arm] = new_value
        m = max(self.values)
        for i in range(len(self.probs)):
            if self.values[i] == m:
                self.probs[i] += self.beta * (1 - self.probs[i])
            else:
                self.probs[i] += self.beta * (0 - self.probs[i])