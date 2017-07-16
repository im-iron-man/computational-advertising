# -*- coding: utf-8 -*-
import time
import numpy as np
import Tkinter as tk

np.random.seed(1)
UNIT = 40
MAZE_H = 4
MAZE_W = 4

class Game(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_W * UNIT))
        self.flag = False
        self._build_maze()

    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white', height=MAZE_H * UNIT, width=MAZE_W * UNIT)
        origin = np.array([20, 20])

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_H * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # create red rect
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red'
        )

        # create hell1
        hell1_center = origin + np.array([UNIT * 2, UNIT])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 15, hell1_center[1] - 15,
            hell1_center[0] + 15, hell1_center[1] + 15,
            fill='black'
        )

        # create hell2
        hell2_center = origin + np.array([UNIT, UNIT * 2])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 15, hell2_center[1] - 15,
            hell2_center[0] + 15, hell2_center[1] + 15,
            fill='black'
        )

        # create oval
        oval_center = origin + UNIT * 2
        self.oval = self.canvas.create_oval(
            oval_center[0] - 15, oval_center[1] - 15,
            oval_center[0] + 15, oval_center[1] + 15,
            fill='yellow'
        )

        self.s = str(self.canvas.coords(self.rect))
        self.canvas.pack()

    def restart(self):
        self.canvas.delete(self.rect)
        origin = np.array([20, 20])
        self.rect = self.canvas.create_rectangle(
            origin[0] - 15, origin[1] - 15,
            origin[0] + 15, origin[1] + 15,
            fill='red'
        )
        self.flag = False
        self.s = str(self.canvas.coords(self.rect))
        return self.s

    def transition(self, action):
        s = self.canvas.coords(self.rect)

        base_action = np.array([0, 0])
        if action == 'u':
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 'd':
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 'r':
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 'l':
            if s[0] > UNIT:
                base_action[0] -= UNIT
        self.canvas.move(self.rect, base_action[0], base_action[1])
        s_ = self.canvas.coords(self.rect)

        if s_ == self.canvas.coords(self.oval):
            reward = 1
            self.flag = True
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2)]:
            reward = -1
            self.flag = True
        else:
            reward = 0

        self.s = str(s_)
        return self.s, reward

    def over(self):
        return self.flag

    def view(self):
        time.sleep(0.1)
        self.update()

if __name__ == '__main__':
    game = Game()
    while not game.over():
        game.view()
        action = raw_input('>>> ')
        s_, reward = game.transition(action)
        print s_, reward
    game.view()
    game.restart()
    while not game.over():
        game.view()
        action = raw_input('>>> ')
        s_, reward = game.transition(action)
        print s_, reward
    game.view()
    game.destroy()