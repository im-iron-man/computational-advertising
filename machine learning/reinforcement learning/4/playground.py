# -*- coding: utf-8 -*-
from environment import Game
from algorithm import QLearn

def play(algo, game, steps):
    for _ in range(steps):
        s = game.restart()
        a = algo.choose(s)
        algo.eligibility_trace *= 0
        game.view()
        while not game.over():
            s_, r = game.transition(a)
            a_ = algo.choose(s_)
            algo.update(s, a, s_, a_, r)
            s = s_
            a = a_
            # print algo.eligibility_trace
            game.view()
        # print _

actions = ['u', 'd', 'l', 'r']
algo = QLearn(actions=actions)
game = Game()
play(algo, game, 100)