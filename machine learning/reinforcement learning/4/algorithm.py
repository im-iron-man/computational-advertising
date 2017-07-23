# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

class QLearn(object):

    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9, trace_decay=0.9):
        self.actions = actions
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.lambda_ = trace_decay
        self.q_table = pd.DataFrame(columns=self.actions)
        self.eligibility_trace = pd.DataFrame(columns=self.actions)

    def choose(self, observation):
        self.check_state_exist(observation)
        if np.random.uniform() < self.epsilon:
            state_action = self.q_table.loc[observation, :]
            state_action = state_action.reindex(np.random.permutation(state_action.index))
            action = state_action.argmax()
        else:
            action = np.random.choice(self.actions)
        return action

    def update(self, s, a, s_, a_, r):
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, a_]
        else:
            q_target = r
        print self.q_table
        print s, a, s_, a_, r
        print q_target, q_predict
        error = q_target - q_predict

        # Method 1
        # self.eligibility_trace.loc[s, a] += 1
        # Method 2
        self.eligibility_trace.loc[s, :] *= 0
        self.eligibility_trace.loc[s, a] = 1
        self.q_table += self.lr * error * self.eligibility_trace
        self.eligibility_trace *= self.gamma * self.lambda_

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            to_be_append = pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state
                )
            self.q_table = self.q_table.append(to_be_append)
            self.eligibility_trace = self.eligibility_trace.append(to_be_append)