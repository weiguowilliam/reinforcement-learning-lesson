import numpy as np
import matplotlib.pyplot as plt
from sarsa_lambda import sarsa_lambda
from windy_setup import *

# initialization 
initial_Q = np.zeros([70,4])
initial_state = stateSpace.index([0,3])
gamma = 1
alpha = 0.5
epsilon = 0.1
num_episodes = 100
action_str=['left','up', 'right', 'down']  

lambdas = np.arange(0,1,0.2)

fig = plt.figure()
for lambda_ in lambdas:
    print('lambda: ',lambda_)
    _, steps,_ = sarsa_lambda(initial_Q, initial_state, transition, 
                         num_episodes, gamma,alpha, lambda_, epsilon)
    episodes = []
    for ep in range(num_episodes):
        episodes.extend([ep] * steps[ep])  
    plt.plot(episodes,label=r'$\lambda$ = ' +str(np.round(lambda_,1)))
    
plt.legend(loc=0)                      
plt.xlabel('Time steps')
plt.ylabel('Episodes')
plt.show()
fig.savefig('windy_sarsaLambda.jpg') 

# larger lambda means larger learning rate.









    
