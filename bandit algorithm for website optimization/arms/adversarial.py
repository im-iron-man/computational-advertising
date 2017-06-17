# -*- coding: utf-8 -*-

class AdversarialArm(object):

    def __init__(self, t, active_start, active_end):
        self.t = t
        self.active_start = active_start
        self.active_end = active_end

    def draw(self):
        self.t += 1
        if self.active_start <= self.t <= self.active_end:
            return 1.0
        else:
            return 0.0