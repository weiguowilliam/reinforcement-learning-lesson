import numpy as np

stateSpace = np.zeros([70,2], dtype=int)
stateSpace[:,0] = np.tile(range(10),7)
stateSpace[:,1] = np.tile(np.repeat(range(7),10),1)
stateSpace = stateSpace.tolist()
terminal_state = [7,3] # state G; state S is [0,3]

wind = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

def transition(state,action):
    # get coordinates of the current state
    state_x, state_y = stateSpace[state]
    
    if action == 0: # left
        next_state = [max(state_x-1,0), min(state_y + wind[state_x], 6)]
   
    elif action == 1: # up
        next_state = [state_x, min(state_y + 1 + wind[state_x], 6)]

    elif action == 2: # right
        next_state = [min(state_x+1,9), min(state_y + wind[state_x], 6)]

    else: # down
        next_state = [state_x, max(min(state_y - 1 + wind[state_x], 6), 0)]

    terminal = next_state == terminal_state

    next_state = stateSpace.index(next_state)
    reward = -1
    
    return next_state, reward, terminal