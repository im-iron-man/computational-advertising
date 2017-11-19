import gym
from RL_brain import DeepQNetwork

env = gym.make('MountainCar-v0')
env = env.unwrapped
RL = DeepQNetwork(n_features=2, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9)

for episode in range(10):
    observation = env.reset()
    ep_r = 0
    while True:
        env.render()
        action = RL.choose_action(observation)
        observation_, reward, done, info = env.step(action)

        # the higher the better
        position, velocity = observation_
        reward = abs(position - (-0.5))     # r in [0, 1]

        ep_r += reward
        RL.learn(observation, action, reward, observation_)
        observation = observation_
        if done:
            print('ep_r: ', ep_r, ' reward: ', reward)
            break