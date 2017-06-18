# -*- coding: utf-8 -*-
import math
import random

class Softmax(object):

    def __init__(self, temperature, n_arms):
        self.temperature = temperature
        self.counts = [0 for _ in range(n_arms)]
        self.values = [0.0 for _ in range(n_arms)]

    def pull(self):
        z = sum([math.exp(v / self.temperature) for v in self.values])
        probs = [math.exp(v / self.temperature) / z for v in self.values]
        t = random.random()
        cum_prob = 0.0
        for i in range(len(probs)):
            cum_prob += probs[i]
            if cum_prob > t:
                return i
        return len(probs) - 1

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        new_value = ((n-1) * value + reward) / n
        self.values[chosen_arm] = new_value

