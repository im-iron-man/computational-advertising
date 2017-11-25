from test import Snake
from test3 import MonteCarloAgent

def monte_carlo_demo(env, agent):
    for episode in range(100):
        r = 0
        env.start()
        while True:
            state = env.pos
            action = agent.policy_act(state)
            reward, state_ = env.action(action)
            agent.store(state, action, reward)
            r += reward
            if state_ == -1:
                print 'episode: {episode} , total reward: {r}'.format(episode=episode, r=r)
                agent.learn()
                break
                
if __name__ == '__main__':
    env = Snake(10, [3, 6])
    agent = MonteCarloAgent(env.state_transition_table(), env.reward_table())
    monte_carlo_demo(env, agent)