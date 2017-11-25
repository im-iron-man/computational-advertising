import numpy as np

class TDAgent:

    def __init__(self, state_transition_table, reward_table):
        self.table = state_transition_table
        self.reward = reward_table
        self.state_num = self.table.shape[1]
        self.act_num = self.table.shape[0]
        self.policy = np.zeros(self.state_num, dtype=np.int)
        self.value_pi = np.zeros((self.state_num))
        self.value_q = np.zeros((self.state_num, self.act_num))
        self.value_n = np.zeros((self.state_num, self.act_num))
        self.gamma = 0.8
        
    def policy_act(self, state):
        if np.random.rand() < 0.05:
            return np.random.randint(self.act_num)
        else:
            return np.argmax(self.value_q[state, :])
            
    def learn(self, state, action, state_, action_, reward):
        self.value_n[state][action] += 1
        self.value_q[state][action] += (reward + (0 if state_ == -1 else self.gamma * self.value_q[state_][action_]) - self.value_q[state][action]) / self.value_n[state][action]