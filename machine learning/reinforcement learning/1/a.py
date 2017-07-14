# -*- coding: utf-8 -*-
import time
import numpy as np
import pandas as pd

np.random.seed(2)

N_STATES = 6
ACTIONS = ['left', 'right']
EPSILON = 0.9
ALPHA = 0.1
LAMBDA = 0.9
MAX_EPISODES = 13
FRESH_TIME = 0.01

def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),
        columns=actions
    )
    return table

def choose_action(state, q_table):
    state_actions = q_table.ix[state, :]
    a = np.random.uniform()
    if a > EPSILON or not state_actions.all():
        action_name = np.random.choice(ACTIONS)
    else:
        action_name = state_actions.argmax()
    return action_name

def get_env_feedback(S, A):
    if A == 'right':
        if S == N_STATES - 2:
            S_, R = 'terminal', 1
        else:
            S_, R = S + 1, 0
    else:
        if S == 0:
            S_, R = 0, 0
        else:
            S_, R = S - 1, 0
    return S_, R

def update_env(S, episode, step_counter):
    env_list = ['-'] * (N_STATES-1) + ['T']
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' % (episode+1, step_counter)
        print '{}'.format(interaction)
        time.sleep(1)
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        print '{}'.format(interaction)
        time.sleep(FRESH_TIME)

def rl():
    q_table = build_q_table(N_STATES, ACTIONS)
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminated = False
        update_env(S, episode, step_counter)
        while not is_terminated:
            A = choose_action(S, q_table)
            S_, R = get_env_feedback(S, A)
            q_predict = q_table.ix[S, A]
            if S_ != 'terminal':
                q_target = R + LAMBDA * q_table.ix[S_, :].max()
            else:
                q_target = R
                is_terminated = True
            q_table.ix[S, A] += ALPHA * (q_target - q_predict)
            S = S_
            update_env(S, episode, step_counter+1)
            step_counter += 1

rl()