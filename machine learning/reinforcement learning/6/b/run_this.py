import gym
from RL_brain import DeepQNetwork

env = gym.make('CartPole-v0')
env = env.unwrapped
RL = DeepQNetwork(env.observation_space.shape[0], learning_rate=0.01, reward_decay=0.9, e_greedy=0.9)

for episode in range(1000):
    observation = env.reset()
    ep_r = 0
    while True:
        env.render()
        action = RL.choose_action(observation)
        observation_, reward, done, info = env.step(action)

        # the smaller theta and closer to center the better
        x, x_dot, theta, theta_dot = observation_
        r1 = (env.x_threshold - abs(x))/env.x_threshold - 0.8
        r2 = (env.theta_threshold_radians - abs(theta))/env.theta_threshold_radians - 0.5
        reward = r1 + r2

        ep_r += reward
        RL.learn(observation, action, reward, observation_)
        observation = observation_
        if done:
            print('ep_r: ', ep_r, ' reward: ', reward)
            break