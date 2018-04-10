import numpy as np
import matplotlib.pyplot as plt
from sarsa import sarsa
from windy_setup import *

# initialization 
initial_Q = np.zeros([70,4])
initial_state = stateSpace.index([0,3])
gamma = 1
alpha = 0.5
epsilon = 0.01
num_episodes = 170
action_str=['left','up', 'right', 'down']  

# using sarsa 
sarsa(initial_Q, initial_state, transition, num_episodes, gamma,alpha, epsilon)