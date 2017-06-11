# -*- coding: utf-8 -*-

def test_algorithm(algo, arms, num_sims, horizon):
    n = num_sims * horizon
    sim_nums = [0.0 for _ in range(n)]
    times = [0.0 for _ in range(n)]
    chosen_arms = [0.0 for _ in range(n)]
    rewards = [0.0 for _ in range(n)]
    cumulative_rewards = [0.0 for _ in range(n)]

    for sim in range(num_sims):
        algo.initialize(len(arms))
        for t in range(horizon):
            chosen_arm = algo.select_arm()
            reward = arms[chosen_arm].draw()
            algo.update(chosen_arm, reward)

            index = sim * horizon + t
            sim_nums[index] = sim + 1
            times[index] = t + 1
            chosen_arms[index] = chosen_arm
            rewards[index] = reward
            if t == 0:
                cumulative_rewards[index] = reward
            else:
                cumulative_rewards[index] = cumulative_rewards[index-1] + reward

    return sim_nums, times, chosen_arms, rewards, cumulative_rewards