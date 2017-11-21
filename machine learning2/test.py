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
        
if __name__ == '__main__':
    env = Snake(10, [3, 6])
    env.start()
    while True:
        reward, state = env.action(1)
        print reward, state
        if state == -1:
            break