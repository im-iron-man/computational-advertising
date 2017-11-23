import numpy as np

class TableAgent:

    def __init__(self, state_transition_table, reward_table):
        self.table = state_transition_table
        self.reward = reward_table
        self.state_num = self.table.shape[1]
        self.act_num = self.table.shape[0]
        self.policy = np.zeros(self.state_num, dtype=np.int)
        self.value_pi = np.zeros((self.state_num))
        self.value_q = np.zeros((self.state_num, self.act_num))
        self.gamma = 0.8
        
    def policy_evaluation(self, iteration_num=None):
        iteration = 0
        while True:
            iteration += 1
            new_value_pi = self.value_pi.copy()
            for i in range(1, self.state_num):
                value_sas = []
                for j in range(0, self.act_num):
                    value_sa = np.dot(self.table[j, i, :], self.reward + self.gamma * self.value_pi)
                    value_sas.append(value_sa)
                new_value_pi[i] = value_sas[self.policy[i]]
            diff = np.sqrt(np.sum(np.power(self.value_pi - new_value_pi, 2)))
            if diff < 1e-6 or (iteration and iteration == iteration_num):
                break
            else:
                self.value_pi = new_value_pi
                
    def policy_improvement(self):
        new_policy = np.zeros_like(self.policy)
        for i in range(1, self.state_num):
            for j in range(0, self.act_num):
                self.value_q[i, j] = np.dot(self.table[j, i, :], self.reward + self.gamma * self.value_pi)
            max_act = np.argmax(self.value_q[i, :])
            new_policy[i] = max_act
        if np.all(np.equal(new_policy, self.policy)):
            return False
        else:
            self.policy = new_policy
            return True
                    
    def policy_iteration(self):
        iteration = 0
        while True:
            iteration += 1
            self.policy_evaluation()
            ret = self.policy_improvement()
            if not ret:
                break
            print 'Iter {} rounds coverge'.format(iteration)
            
    def value_iteration(self, iteration_num=None):
        iteration = 0
        while True:
            iteration += 1
            new_value_pi = np.zeros_like(self.value_pi)
            for i in range(1, self.state_num):
                value_sas = []
                for j in range(0, self.act_num):
                    value_sa = np.dot(self.table[j, i, :], self.reward + self.gamma * self.value_pi)
                    value_sas.append(value_sa)
                new_value_pi[i] = max(value_sas)
            diff = np.sqrt(np.sum(np.power(self.value_pi - new_value_pi, 2)))
            if diff < 1e-6 or (iteration_num and iteration == iteration_num):
                break
            else:
                self.value_pi = new_value_pi
            print 'Iter {} rounds converge'.format(iteration)
            
        for i in range(1, self.state_num):
            for j in range(0, self.act_num):
                self.value_q[i, j] = np.dot(self.table[j, i, :], self.reward + self.gamma * self.value_pi)
            max_act = np.argmax(self.value_q[i, :])
            self.policy[i] = max_act
    
    def generalized_policy_iteration(self):
        self.value_iteration(10)
        self.policy_iteration(1)