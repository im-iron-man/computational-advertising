from test import Snake
from test1 import TableAgent

def eval(env, agent):
    r = 0
    env.start()
    while True:
        a = agent.policy[env.pos]
        reward, state = env.action(a)
        r += reward
        if state == -1:
            break
    return r
    
def simple_eval():
    env = Snake(0, [3, 6])
    agent = TableAgent(env.state_transition_table(), env.reward_table())
    print 'return3={}'.format(eval(env, agent))
    agent.policy[:] = 1
    print 'return6={}'.format(eval(env, agent))
    agent.policy[97:100] = 0
    print 'return_ensemeble={}'.format(eval(env, agent))
    
def policy_iteration_demo():
    env = Snake(0, [3, 6])
    agent = TableAgent(env.state_transition_table(), env.reward_table())
    agent.policy_iteration()
    print 'return_pi={}'.format(eval(env, agent))
    print agent.policy
    
def policy_iteration_demo2():
    env = Snake(10, [3,6])
    agent = TableAgent(env.state_transition_table(), env.reward_table())
    print 'return3={}'.format(eval(env, agent))
    agent.policy[:] = 1
    print 'return6={}'.format(eval(env, agent))
    agent.policy[97:100] = 0
    print 'return_ensemble={}'.format(eval(env, agent))
    agent.policy_iteration()
    print 'return_pi={}'.format(eval(env, agent))
    print agent.policy
    
def policy_iteration_demo3():
    env = Snake(10, [3,6])
    agent = TableAgent(env.state_transition_table(), env.reward_table())
    print 'return3={}'.format(eval(env, agent))
    agent.policy[:] = 1
    print 'return6={}'.format(eval(env, agent))
    agent.policy[97:100] = 0
    print 'return_ensemble={}'.format(eval(env, agent))
    agent.value_iteration()
    print 'return_pi={}'.format(eval(env, agent))
    print agent.policy
    
def policy_iteration_demo4():
    env = Snake(10, [3,6])
    agent = TableAgent(env.state_transition_table(), env.reward_table())
    print 'return3={}'.format(eval(env, agent))
    agent.policy[:] = 1
    print 'return6={}'.format(eval(env, agent))
    agent.policy[97:100] = 0
    print 'return_ensemble={}'.format(eval(env, agent))
    agent.generalized_policy_iteration()
    print 'return_pi={}'.format(eval(env, agent))
    print agent.policy

if __name__ == '__main__':
    simple_eval()
    policy_iteration_demo()
    policy_iteration_demo2()
    policy_iteration_demo3()
    policy_iteration_demo4()