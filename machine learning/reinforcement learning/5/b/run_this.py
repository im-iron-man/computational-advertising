from maze_env import Maze
from RL_brain import DeepQNetwork


def run_maze():
    for episode in range(1000):
        observation = env.reset()
        while True:
            env.render()
            action = RL.choose_action(observation)
            observation_, reward, done = env.step(action)
            RL.learn(observation, action, reward, observation_)
            observation = observation_
            if done:
                break
    print('game over')
    env.destroy()


if __name__ == "__main__":
    env = Maze()
    RL = DeepQNetwork(env.n_features, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9)
    env.after(100, run_maze)
    env.mainloop()