# //
# //                       _oo0oo_
# //                      o8888888o
# //                      88" . "88
# //                      (| -_- |)
# //                      0\  =  /0
# //                    ___/`---'\___
# //                  .' \\|     |// '.
# //                 / \\|||  :  |||// \
# //                / _||||| -:- |||||- \
# //               |   | \\\  -  /// |   |
# //               | \_|  ''\---/''  |_/ |
# //               \  .-\__  '-'  ___/-. /
# //             ___'. .'  /--.--\  `. .'___
# //          ."" '<  `.___\_<|>_/___.' >' "".
# //         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
# //         \  \ `_.   \_ __\ /__ _/   .-` /  /
# //     =====`-.____`.___ \_____/___.-`___.-'=====
# //                       `=---='
# //
# game link: http://people.virginia.edu/~mtp4be/MaskingGame_FRL_2018/
import random
import numpy as np
import math
import time
import pyautogui as pag
import glob
import pandas as pd
import os
import json as js
import gym
import tensorflow as tf
from collections import deque
from dqn_final import *
from mouse_final import *
import matplotlib  
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd


#####################
## final ############
#####################

STEP = 61 # Step limitation in an episode
TEST = 10 # The number of experiment test every 100 episode

def main(epi, num_test):
    EPISODE = epi # Episode limitation
    STEP = 61 # Step limitation in an episode
    TEST = 10 # The number of experiment test every 100 episode

    agent = DQN()

    time.sleep(3)
    for i in range(22):
        pag.typewrite('p')
    
    grade_list = []
    reward1_list = []
    reward2_list = []
    reward3_list = []

    for episode in range(EPISODE):
        print(episode)
        terminal = False

        episode += 1
        state = get_random_state()
        action = get_random_state()
        pag.moveTo(150, 370-action * 10)
        y_list = [0,0,0,0]
        y_list_next = [0,0,0,0]
        y_coors = []
        previous_y = np.zeros(61)

        num_for_reward = 0 # from 0 to 180
        while terminal == False:
            num_for_reward += 1
            # next_state,reward,done,y_list[0],y_list[1],y_list[2],y_list[3],y_list_next[0],y_list_next[1],y_list_next[2], y_list_next[3] = draw_step(s = state, a = action, y_coors = y_coors)
            next_state,reward,done,y_list[0],y_list[1],y_list[2],y_list[3],y_list_next[0],y_list_next[1],y_list_next[2], y_list_next[3],previous_y = draw_step(s = state, a = action, y_coors = y_coors,pre_y = previous_y)
            #first line reward
            if (num_for_reward == 60):
                reward1_list.append(reward)
            #second line reward
            if (num_for_reward == 121):
                reward2_list.append(reward)
            #third line reward
            if (num_for_reward == 182):
                reward3_list.append(reward)
            
            agent.perceive(y_list,action,reward,y_list_next,done)
            next_action = agent.egreedy_action(y_list) # e-greedy action for train
            
            state = next_state
            action = next_action
            if done:
                break
        
        grade = read_grade()
        grade_list.append(grade)


        time.sleep(1)
        pag.press('p')
        pag.typewrite('p')
        time.sleep(1)
        pag.press('n')
        pag.typewrite('n')
        time.sleep(1)
        deletefile()

    #test after the first num_episodes episodes
    for episode in range(num_test):
        terminal = False

        episode += 1
        state = get_random_state()
        action = get_random_state()
        pag.moveTo(150, 370-action * 10)
        y_list = [0,0,0,0]
        y_list_next = [0,0,0,0]
        y_coors = []
        previous_y = np.zeros(61)

        while terminal == False:
            # next_state,reward,done,y_list[0],y_list[1],y_list[2],y_list[3],y_list_next[0],y_list_next[1],y_list_next[2], y_list_next[3] = draw_step(s = state, a = action, y_coors = y_coors)
            next_state,reward,done,y_list[0],y_list[1],y_list[2],y_list[3],y_list_next[0],y_list_next[1],y_list_next[2], y_list_next[3],previous_y = draw_step(s = state, a = action, y_coors = y_coors,pre_y = previous_y)
            agent.perceive(y_list,action,reward,y_list_next,done)
            next_action = agent.action(y_list) # direct get action from q table
            # print(q_list)
            
            state = next_state
            action = next_action
            if done:
                break


        time.sleep(1)
        pag.press('p')
        pag.typewrite('p')
        time.sleep(1)
        pag.press('n')
        pag.typewrite('n')
        time.sleep(1)
        deletefile()

    # plt.plot(grade_list)
    # plt.show()
    # my_df = pd.DataFrame(grade_list)
    my_df = pd.DataFrame({"reward1":reward1_list,"reward2":reward2_list,"reward3":reward3_list,"grade":grade_list})
    my_df.to_csv('out.csv', index=True, header=True)
    



###################
##               ##
##  RUN          ##
##               ##
###################

main(epi = 1, num_test = 0)