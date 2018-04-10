import numpy as np

def MCES(get_episode,initial_Q,initial_policy,gamma,alpha,num_episodes=1e4):
    # This function implements the Monte Carlo ES algorithm. 
    # It returns the learned Q values and the greedy policy w.r.t. Q.
    
    # If alpha = 0, update Q[s,a] += (G - Q[s,a]) / N_sa[s,a];
    # otherwise, Q[s,a] += (G - Q[s,a]) * alpha

    # initialization  
    Q = np.copy(initial_Q)
    policy = np.copy(initial_policy)
    num_states, num_actions = Q.shape
    N_sa = np.zeros([num_states, num_actions]) #counter of (s,a)
    
    iteration = 0
    
    while iteration < num_episodes:

        """
        Your code
        """
        states, actions, rewards = get_episode(initial_policy)
        G = 0
        # count N, what if same s with different a
        dic = {}
        for s in range(len(rewards)):
            if states[s] not in dic.keys() or dic[states[s]] != actions[s]:
                dic[states[s]] = actions[s]
                N_sa[states[s], actions[s]] += 1
        # calculate G
        for i in range(len(rewards)):
            for j in range(i, len(rewards)):
                G += rewards[i] * gamma ** j
            # update Q
            if alpha == 0:
                Q[states[i], actions[i]] += (G - Q[states[i], actions[i]]) / N_sa[states[i], actions[i]]
            else:
                Q[states[i], actions[i]] += (G - Q[states[i], actions[i]]) * alpha
            # update policy
            Q_max = Q[states[i], actions[0]]
            for a in range(len(actions)):
                if Q[states[i], actions[a]] > Q_max:
                    policy[states[i], actions[a]] = 1
        iteration += 1                                        
        
    return Q , policy

