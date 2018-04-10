import numpy as np

def q_learn(initial_Q,initial_state,transition,
          num_episodes,gamma, alpha, epsilon=0.1):
              
    """
    This function implements Q-learning. It returns learned Q values.
    To crete 6.4, the function also returns number of steps, and 
    the total rewards in each episode.
        
    Notes on inputs:    
    -transition: function. It takes current state s and action a as parameters 
                and returns next state s', immediate reward R, and a boolean 
                variable indicating whether s' is a terminal state. 
                (See windy_setup as an example)
    -epsilon: exploration rate as in epsilon-greedy policy
    
    """    
    
    """ 
    Your code
    """
            
    return Q,  steps, rewards