import numpy as np
import matplotlib.pyplot as plt
from sarsa import sarsa
from windy9_setup import *

# initialization 
initial_Q = np.zeros([70,9])
initial_state = stateSpace.index([0,3])
gamma = 1
alpha = 0.5
epsilon = 0.01
num_episodes = 170
action_str=['left','up', 'right', 'down', 
            'up/left', 'up/right', 'down/right', 'down/left', 'stand'] 
# using sarsa 
Q, steps,rewards = sarsa(initial_Q, initial_state, transition, 
                         num_episodes, gamma,alpha, epsilon)

# plot episodes vs time steps, i.e., figure 6.3
episodes = []
for ep in range(num_episodes):
    episodes.extend([ep] * steps[ep])
fig = plt.figure()
plt.plot(episodes)
plt.xlabel('Time steps')
plt.ylabel('Episodes')
plt.show()
#fig.savefig('windy9.jpg')

# print the optimal route
actions = np.argmax(Q,axis=1)
state = initial_state
num_steps = 0    
terminal = False
print('optimal route:')
while not terminal and num_steps < 15:        
    action = actions[state]
    print('state:',stateSpace[state],'  action:',action_str[action])
    next_state,_,terminal = transition(state,action)

    state = next_state
    num_steps += 1
if num_steps < 8:
    print('state:', '[7,3]')
    print('number of steps: ', num_steps)
else:
    print('Cannot terminate in 7 steps. Run again')



    
 
