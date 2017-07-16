# -*- coding: utf-8 -*-
from environment import Game
from algorithm import QLearn

def play(algo, game, steps):
    for _ in range(steps):
        s = game.restart()
        game.view()
        while not game.over():
            a = algo.choose(s)
            s_, r = game.transition(a)
            algo.update(s, a, s_, r)
            s = s_
            game.view()

actions = ['l', 'r' ,'u', 'd']
algo = QLearn(actions=actions)
game = Game()
play(algo, game, 100)