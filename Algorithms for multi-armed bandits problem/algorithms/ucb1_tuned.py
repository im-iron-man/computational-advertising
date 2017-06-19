# -*- coding: utf-8 -*-
import math

class UCB1Tuned(object):

    def __init__(self, n_arms):
        self.counts = [0 for _ in range(n_arms)]
        self.values = [0.0 for _ in range(n_arms)]
        self.variances = [0.0 for _ in range(n_arms)]

    def pull(self):
        n_arms = len(self.counts)
        for arm in range(n_arms):
            if self.counts[arm] == 0:
                return arm
        ucb_values = [0.0 for _ in range(n_arms)]
        total_counts = sum(self.counts)
        for arm in range(n_arms):
            v = self.variances[arm] + math.sqrt(2 * math.log(total_counts) / self.counts[arm])
            bonus = math.sqrt(math.log(total_counts) / self.counts[arm] * min(0.25, v))
            ucb_values[arm] = self.values[arm] + bonus
        m = max(ucb_values)
        return ucb_values.index(m)

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        new_value = ((n-1) * value + reward) / n
        self.values[chosen_arm] = new_value
        variance = self.variances[chosen_arm]
        new_variance = 1.0 * (n-1) / n * variance + 1.0 * (n-1) / n ** 2 * (reward - value) ** 2
        self.variances[chosen_arm] = new_variance