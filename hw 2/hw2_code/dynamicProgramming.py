import numpy as np

def policyEval(policy, P, R, gamma, theta, max_iter=1e8):
    """
    This function implements the policy evaluation algorithm (the synchronous
    version) 
    It returns state value function v_pi.
    """    
    num_S, num_a = policy.shape    
    v = np.zeros(num_S) # initialize value function
    k = 0 # counter of iteration
    
    """
    
    Your code

    """
    
    return v
    

def policyImprv(P,R,gamma,policy,v):
    """
    This function implements the policy improvement algorithm.
    It returns the improved policy and a boolean variable policy_stable (True
    if the new policy is the same as the old policy)
    """
    # initialization    
    num_S, num_a = policy.shape
    policy_new = np.zeros([num_S,num_a])
    policy_stable = True
        
    """
    
    Your code 
    
    """
    
    return policy_new, policy_stable


def policyIteration(P,R,gamma,theta,initial_policy,max_iter=1e6):
    """
    This function implements the policy iteration algorithm.
    It returns the final policy and the corresponding state value function v.
    """
    policy_stable = False
    policy = np.copy(initial_policy)
    num_iter = 0
    
    while (not policy_stable) and num_iter < max_iter:
        num_iter += 1
        print('Policy Iteration: ', num_iter)
        # policy evaluation
        v = policyEval(policy,P,R,gamma,theta)
        # policy improvement
        policy, policy_stable = policyImprv(P,R,gamma,policy,v)
    return policy, v



def valueIteration(P,R,gamma,theta,initial_v,max_iter=1e8):
    """
    This function implements the value iteration algorithm (the in-place version).
    It returns the best action for each state  under a deterministic policy, 
    and the corresponding state-value function.
    """
    print('Running value iteration ...')    
    
    # initialization
    v = initial_v    
    num_states, num_actions = P.shape[:2]
    k = 0 
    best_actions = [0] * num_states
    
    """
    
    Your code
    
    """
    
    print('number of iterations:', k)
    return best_actions, v