# -*- coding:utf-8 -*-
import random
from algorithms.epsilon_greedy import EpsilonGreedy
from arms.bernoulli import BernoulliArm
from tests.test_framework import test_algorithm

random.seed(1)
means = [0.1, 0.1, 0.1, 0.1, 0.9]
random.shuffle(means)
arms = map(lambda mu: BernoulliArm(mu), means)

f = open('demo.tsv', 'w')
algo = EpsilonGreedy(0.1, [], [])
results = test_algorithm(algo, arms, 5000, 250)
for i in range(len(results[0])):
    f.write(str(0.1) + '\t')
    f.write('\t'.join([str(results[j][i]) for j in range(len(results))]) + '\n')
f.close()