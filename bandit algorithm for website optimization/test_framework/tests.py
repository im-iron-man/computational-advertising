# -*- coding: utf-8 -*-

def test_algorithm(algo, arms, num_sims, horizon):
    n = num_sims * horizon
    chosen_arms = [0.0 for _ in range(n)]
    rewards = [0.0 for _ in range(n)]
    cumulative_rewards = [0.0 for _ in range(n)]
    sim_nums = [0.0 for _ in range(n)]
    times = [0.0 for _ in range(n)]

    for sim in range(num_sims):
        sim += 1
        algo.initialize(len(arms))
        for t in range(horizon):
            t += 1
            index = (sim - 1) * horizon + t - 1
            sim_nums[index] = sim
            times[index] = t
            chosen_arm = algo.select_arm()
            chosen_arms[index] = chosen_arm
            reward = arms[chosen_arms[index]].draw()
            rewards[index] = reward
            if t == 1:
                cumulative_rewards[index] = reward
            else:
                cumulative_rewards[index] = cumulative_rewards[index-1] + reward
            algo.update(chosen_arm, reward)

    return sim_nums, times, chosen_arms, rewards, cumulative_rewards