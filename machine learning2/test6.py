from test import Snake
from test5 import TDAgent

def temporal_difference_demo(env, agent):
    for episode in range(100):
        r = 0
        env.start()
        state = env.pos
        action = agent.policy_act(state)
        while True:
            reward, state_ = env.action(action)
            action_ = agent.policy_act(state)
            agent.learn(state, action, state_, action_, reward)
            r += reward
            if state_ == -1:
                print 'episode: {episode} , total reward: {r}'.format(episode=episode, r=r)
                break
                
if __name__ == '__main__':
    env = Snake(10, [3, 6])
    agent = TDAgent(env.state_transition_table(), env.reward_table())
    temporal_difference_demo(env, agent)