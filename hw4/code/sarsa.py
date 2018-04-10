import numpy as np
import random

def sarsa(initial_Q,initial_state,transition,
          num_episodes,gamma, alpha, epsilon=0.1):
    """
    This function implements Sarsa. It returns learned Q values.
    To crete Figure 6.3 and 6.4, the function also returns number of steps, and 
    the total rewards in each episode.
        
    Notes on inputs:    
    -transition: function. It takes current state s and action a as parameters 
                and returns next state s', immediate reward R, and a boolean 
                variable indicating whether s' is a terminal state. 
                (See windy_setup as an example)
    -epsilon: exploration rate as in epsilon-greedy policy
    
    """    
    
    def egreedy(epsilon, Q_row):
        r = random.uniform(0,1)
        maxq_action = Q_row.argmax()
        if(r>epsilon):
            this_action = maxq_action
        
        else:#random choice all actions, if get best action, choice again
            this_action_original = random.choice(list(range(4)))
            while(this_action_original == maxq_action):
                this_action_original = random.choice(list(range(4)))
            this_action = this_action_original
        
        return this_action


    # initialization    
    Q = np.copy(initial_Q)
    num_states, num_actions = Q.shape    
       
    steps = np.zeros(num_episodes,dtype=int) # store #steps in each episode
    rewards = np.zeros(num_episodes) # store total rewards for each episode
  
    for ep in range(num_episodes):
        print(str(ep)+" episodes")
        #choose action from present state with epsilon-greedy policy
        terminal = False
        this_state = initial_state
        rewards_in_episode = 0
        steps_in_episode = 1

        this_action = egreedy(epsilon, Q[this_state,:])

        print("initial state is"+str(this_action))
        while (terminal == False):
            steps_in_episode += 1
        
            next_state, reward, terminal = transition(state = this_state , action = this_action)
            rewards_in_episode += reward

            next_action = egreedy(epsilon, Q[next_state,:])

           
            print("calculated next action")
            Q[this_state, this_action] += alpha * (reward + gamma*Q[next_state, next_action] - Q[this_state, this_action])
            this_state = next_state
            this_action = next_action
            print("iteration")

        #get terminal
        rewards[ep] = rewards_in_episode
        steps[ep] = steps_in_episode
        print("end episodes")
    return Q,  steps, rewards


# optimal route:
# state: [0, 3]   action: right
# state: [1, 3]   action: right
# state: [2, 3]   action: right
# state: [3, 3]   action: right
# state: [4, 4]   action: right
# state: [5, 5]   action: right
# state: [6, 6]   action: right
# state: [7, 6]   action: right
# state: [8, 6]   action: right
# state: [9, 6]   action: down
# state: [9, 5]   action: down
# state: [9, 4]   action: down
# state: [9, 3]   action: down
# state: [9, 2]   action: left
# state: [8, 2]   action: left
# state: [7,3]
# number of steps:  15