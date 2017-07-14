# -*- coding: utf-8 -*-
import time
import numpy as np
import pandas as pd

class QLearn(object):

    def __init__(self, epsilon, alpha, beta, states, actions):
        self.table = pd.DataFrame(np.zeros((len(states), len(actions))), index=states, columns=actions)
        self.epsilon = epsilon
        self.alpha = alpha
        self.beta = beta
        self.states = states
        self.actions = actions

    def choose(self, state):
        state_actions = self.table.loc[state, :]
        a = np.random.uniform()
        if a > self.epsilon or not state_actions.all():
            action = np.random.choice(self.actions)
        else:
            action = state_actions.argmax()
        return action

    def update(self, old_state, action, new_state, reward):
        predict = self.table.loc[old_state, action]
        if new_state != self.states[-1]:
            target = reward + self.beta * self.table.loc[new_state, :].max()
        else:
            target = reward
        self.table.loc[old_state, action] += self.alpha * (target - predict)

class Game(object):

    def __init__(self, n):
        self.n = n
        self.state = 1

    def trans(self, action):
        if action == 'right':
            if self.state == self.n - 1:
                self.state = 'Terminal'
                reward = 1
            else:
                self.state += 1
                reward = 0
        else:
            if self.state == 1:
                self.state = 1
                reward = 0
            else:
                self.state -= 1
                reward = 0
        return self.state, reward

    def over(self):
        return self.state == 'Terminal'

    def view(self):
        env_list = ['-'] * (self.n - 1) + ['T']
        if not self.over():
            env_list[self.state-1] = 'o'
        print ''.join(env_list)

def reinforcement_learning(algo, games):
    np.random.seed(2)
    for game in games:
        step = 0
        game.view()
        while not game.over():
            old_state = game.state
            action = algo.choose(old_state)
            new_state, reward = game.trans(action)
            algo.update(old_state, action, new_state, reward)
            step += 1
            game.view()
        print 'total steps: %d' % step
        time.sleep(1)

qlearn = QLearn(epsilon=0.9, alpha=0.1, beta=0.9, states=[1, 2, 3, 4, 5, 'Terminal'], actions=['left', 'right'])
games = [Game(6) for _ in range(13)]
reinforcement_learning(qlearn, games)