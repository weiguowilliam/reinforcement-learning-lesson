import numpy as np
import random
from blackjack_setup import *


def MCES(get_episode,initial_Q,initial_policy,gamma,alpha,num_episodes=1e4):
    # This function implements the Monte Carlo ES algorithm. 
    # It returns the learned Q values and the greedy policy w.r.t. Q.
    
    # If alpha = 0, update Q[s,a] += (G - Q[s,a]) / N_sa[s,a];
    # otherwise, Q[s,a] += (G - Q[s,a]) * alpha

    # initialization  
    Q = np.copy(initial_Q)
    policy = np.copy(initial_policy)
    num_states, num_actions = Q.shape
    N_sa = np.zeros([num_states,num_actions]) #counter of (s,a)
    
    iteration = 0
    
    while iteration < num_episodes:

        """
        Your code
        """
        iteration += 1
        states, actions, rewards = get_episode(policy)
        G = 0
        # count N, what if same s with different a
        dic_G = {}
        for s in range(len(rewards)):
            if states[s] not in dic_G.keys():
                dic_G[states[s]] = actions[s]
                N_sa[states[s], actions[s]] += 1

        for i in range(len(rewards)):
            for j in range(i, len(rewards)):
                G += rewards[i] * gamma ** j

            if alpha == 0:
                Q[states[i], actions[i]] += (G - Q[states[i], actions[i]]) / N_sa[states[i], actions[i]]
            else:
                Q[states[i], actions[i]] += (G - Q[states[i], actions[i]]) * alpha
            
        


        # iteration += 1 

        # states, actions, rewards = get_episode(policy)
        # G_dic = {} # G_dic is dictionary to save each (s,a) pair
        # for r in range(len(rewards)):
        #     N_sa[states[r],actions[r]] += 1
        #     if (states[r],actions[r]) not in G_dic.keys():
        #         G_dic[(states[r],actions[r])] = 0



        # #calculate G for each (state, action) pair
        # for t in range(len(rewards)):
        #     if G_dic[(states[t],actions[t])] == 0: # =0 means the (s,a) pair is the first time appear
        #         G = 0
        #         for k in range(t, len(rewards)):
        #             G += rewards[k] * gamma ** (k-t)

        #         if alpha == 0:
        #             Q[states[t],actions[t]] += (G - Q[states[t],actions[t]]) / N_sa[states[t],actions[t]]
        #         else:
        #             Q[states[t],actions[t]] += (G - Q[states[t],actions[t]]) * alpha 
                
    return Q , policy

