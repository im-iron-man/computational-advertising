import numpy as np

class TableAgent:

    def __init__(self, state_transition_table, reward_table):
        self.table = state_transition_table
        self.reward = reward_table
        self.state_num = self.table.shape[1]
        self.act_num = self.table.shape[0]
        self.policy = no.zeros(self.state_num, dtype=np.int)
        self.value_pi = np.zeros((self.state_num))
        self.value_q = np.zeros((self.state_num, self.act_num))
        self.gamma = 0.8