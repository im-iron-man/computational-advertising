# -*- coding: utf-8 -*-

def test_algorithm(algo, arms, horizon):
    times = [0.0 for _ in range(horizon)]
    chosen_arms = [0.0 for _ in range(horizon)]
    rewards = [0.0 for _ in range(horizon)]
    cumulative_rewards = [0.0 for _ in range(horizon)]

    for t in range(horizon):
        chosen_arm = algo.pull()
        reward = arms[chosen_arm].draw()
        algo.update(chosen_arm, reward)

        times[t] = t + 1
        chosen_arms[t] = chosen_arm
        rewards[t] = reward
        if t == 0:
            cumulative_rewards[t] = reward
        else:
            cumulative_rewards[t] = cumulative_rewards[t-1] + reward

    return times, chosen_arms, rewards, cumulative_rewards