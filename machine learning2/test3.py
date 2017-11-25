import numpy as np

class MonteCarloAgent:

    def __init__(self, state_transition_table, reward_table):
        self.table = state_transition_table
        self.reward = reward_table
        self.state_num = self.table.shape[1]
        self.act_num = self.table.shape[0]
        self.policy = np.zeros(self.state_num, dtype=np.int)
        self.value_pi = np.zeros((self.state_num))
        self.value_q = np.zeros((self.state_num, self.act_num))
        self.value_n = np.zeros((self.state_num, self.act_num))
        self.episode = []
        self.gamma = 0.8
             
    def policy_act(self, state):
        if np.random.rand() < 0.05:
            return np.random.randint(self.act_num)
        else:
            return np.argmax(self.value_q[state, :])
        
    def store(self, state, action, reward):
        self.episode.append((state, action, reward))
        
    def learn(self):
        value = []
        return_val = 0
        for item in reversed(self.episode):
            return_val = return_val * self.gamma + item[2]
            self.value_n[item[0]][item[1]] += 1
            self.value_q[item[0]][item[1]] += (return_val - self.value_q[item[0]][item[1]]) / self.value_n[item[0]][item[1]]
            
            