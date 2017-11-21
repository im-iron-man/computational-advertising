import numpy as np

class Snake:
    
    def __init__(self, ladder_num, dice_ranges):
        self.ladder_num = ladder_num
        self.dice_ranges = dice_ranges
        self.ladders = dict(np.random.randint(1, 100, size=(ladder_num, 2)))
        reverse_ladders = [(v, k) for k, v in self.ladders.items()]
        for item in reverse_ladders:
            self.ladders[item[0]] = item[1]
        print 'ladders info:'
        print self.ladders
        print 'dice ranges:'
        print self.dice_ranges
        
    def start(self):
        self.pos = 1
        
    def action(self, act):
        step = np.random.randint(1, self.dice_ranges[act]+1)
        self.pos += step
        if self.pos == 100:
            return 100, -1
        elif self.pos > 100:
            self.pos = 200 - self.pos
        if self.pos in self.ladders:
            self.pos = self.ladders[self.pos]
        return -1, self.pos
        
    def state_transition_table(self):
        table = np.zeros((len(self.dice_ranges), 101, 101))
        ladder_move = np.vectorize(lambda x: self.ladders[x] if x in self.ladders else x)
        for i, dice in enumerate(self.dice_ranges):
            prob = 1.0 / dice
            for s in range(1, 100):
                step = np.arange(dice)
                step += s
                step = np.piecewise(step, [step > 100, step <= 100], [lambda x: 200 - x, lambda x: x])
                step = ladder_move(step)
                for final_move in step:
                    table[i, s, final_move] += prob
        table[:, 100, 100] = 1
        return table
        
    def reward_table(self):
        table = np.array([-1] * 101)
        table[100] = 100
        return table
        
if __name__ == '__main__':
    env = Snake(10, [3, 6])
    env.start()
    while True:
        reward, state = env.action(1)
        print reward, state
        if state == -1:
            break