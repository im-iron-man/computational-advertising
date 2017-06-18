# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from algorithms.epsilon_greedy import EpsilonGreedy
from arms.bernoulli import BernoulliArm
from tests.test_framework import test_algorithm

algo = EpsilonGreedy(0.1, 5)
means = [0.1, 0.1, 0.1, 0.1, 0.9]
arms = map(lambda mu: BernoulliArm(mu), means)
times, chosen_arms, rewards, cumulative_rewards = test_algorithm(algo, arms, 500)

# accuracy of the Epsilon Greedy Algorithm
best_arms = [0.0 for _ in range(len(times))]
for t in times:
    if chosen_arms[t-1] == 4:
        if t == 1:
            best_arms[t-1] = 1.0
        else:
            best_arms[t-1] = 1.0 * (best_arms[t-2] * (t-1) + 1) / t
    else:
        if t == 1:
            best_arms[t-1] = 0.0
        else:
            best_arms[t-1] = 1.0 * best_arms[t-2] * (t-1) / t
plt.subplot(221)
plt.plot(times, best_arms)
plt.grid()

# Performance of the Epsilon Greedy Algorithm
average_rewards = [0.0 for _ in range(len(times))]
for t in times:
    average_rewards[t-1] = cumulative_rewards[t-1] / t
plt.subplot(222)
plt.plot(times, average_rewards)
plt.grid()

# Cumulative Reward of the Epsilon Greedy Algorithm
plt.subplot(223)
plt.plot(times, cumulative_rewards)
plt.grid()

plt.show()