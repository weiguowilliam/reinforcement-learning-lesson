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


#########################
## Mouse Behavior  ######
#########################


def deletefile():
    test_report = "/Users/guowei/Downloads/js"
    lists = os.listdir(test_report)
    for f in lists:
        if "saved" not in f:
            os.remove(os.path.join(test_report, f))

def get_random_state():
    a = random.randint(0,4)
    return a

def get_random_action():
    a = random.randint(0,7)
    return a

def next_line(a):
    pag.moveTo(150,370- a*10,0.1)

def one_movement(x,a):
    pag.moveTo(x+10,370- a*10,0.1)

def get_next_state(s,a):
    a = get_random_action()

def draw_step(s, a, y_coors, pre_y):
    

    step = int((s - 1) / 488)

    sum = s - step * 488

    x = int((sum - 1) / 8)

    y = sum - x * 8

    x_coor = 150 + 10 * x

    y_coor = 370 - 10 * (y - 1)

    # x_coors += [x_coor]
    y_coors += [y_coor]

    current_y = pre_y

    if step == 2 and x == 60:
        time.sleep(0.5)
        pag.press('esc')

        s = 488 * 3 + 1
        R = 0
        status = True
        return s, R, status, y_coors[182], y_coors[181], current_y[60], current_y[60], y_coors[182], y_coors[182], \
               current_y[60], current_y[60],pre_y


    elif step == 1 and x == 60:
        pag.press('esc')
        pag.press('p')
        pag.typewrite('p')
        time.sleep(2)

        R = 0
        status = False

        s = 488 * 2 + a + 1

        next_line(a)

        pag.press('enter')

        return s, R, status, y_coors[121], y_coors[120], current_y[60], current_y[60], y_coors[121], y_coors[121], current_y[60], current_y[60],pre_y

    elif step == 0 and x == 60:

        R = 0
        status = False
        s = 488 + a

        next_line(a)
        pag.press('enter')
        return s, R, status, y_coors[60], y_coors[59], 371, 371, y_coors[60], y_coors[60], 371, 371,pre_y

    elif step == 2 and x == 59:

        
        status = False
        s = 488 + 488 + 480 + a + 1

        one_movement(x_coor, a)

        pag.press('esc')
        pag.press('p')
        pag.typewrite('p')
        time.sleep(2)
        try:
            R = readreward2()
        except IndexError:
            print("readreward2 error")
            pag.press('p')
            pag.typewrite('p')
            time.sleep(2)
            R = readreward2()
        return s, R, status, y_coors[181], y_coors[180], y_coors[120], y_coors[121], 370 - a * 10, y_coors[181], \
               y_coors[121], y_coors[121],pre_y

    elif step == 1 and x == 59:

        status = False
        s = 488 + 480 + a + 1
        one_movement(x_coor, a)

        pag.press('esc')
        pag.press('p')
        pag.typewrite('p')
        time.sleep(2)
        R = readreward()

        length, previous_xlist, previous_ylist = get_previous_line()
        pre_y = calculate_y(length, previous_xlist, previous_ylist)
        #print previous_y

        return s, R, status, y_coors[120], y_coors[119], current_y[59], current_y[60], 370 - a * 10, y_coors[120], current_y[60], current_y[60],pre_y

    elif step == 0 and x == 59:

        status = False

        s = 480 + a + 1

        one_movement(x_coor, a)
        pag.press('esc')
        pag.press('p')
        pag.typewrite('p')
        time.sleep(2)
        try:
            R = readreward()
        except IndexError:
            print("readreward error")
            pag.press('p')
            pag.typewrite('p')
            time.sleep(2)
            R = readreward()
        length, previous_xlist, previous_ylist = get_previous_line()
        pre_y = calculate_y(length, previous_xlist, previous_ylist)
        #print previous_y



        return s, R, status, y_coors[59], y_coors[58], 371, 371, 370 - a * 10, y_coors[59], 371, 371,pre_y

    elif step == 0 and x == 0:

        R = 0
        status = False
        s = (x + 1) * 8 + a + 1
        pag.press('enter')

        one_movement(x_coor, a)

        return s, R, status, y_coors[0], y_coors[0], 371, 371, 370 - a * 10, y_coors[0], 371, 371,pre_y

    elif x == 0:

        R = 0
        status = False
        s = step * 488 + (x + 1) * 8 + a + 1
        one_movement(x_coor, a)

        return s, R, status, y_coors[x + 61 * step], y_coors[x + 61 * step], current_y[x], current_y[x+1], 370 - a * 10, y_coors[x + 61 * step], current_y[x+1],current_y[x+2],pre_y






    elif step == 0:

        R = 0
        status = False
        s = (x + 1) * 8 + a + 1

        one_movement(x_coor, a)
        return s, R, status, y_coors[x], y_coors[x - 1], 371, 371, 370 - a * 10, y_coors[x], 371, 371,pre_y

    else:
        # R = 0
        if y_coor > current_y[x] and y_coors[x +61*step -1] > current_y[x-1]:
            R = 1
        elif y_coor < current_y[x] and y_coors[x +61*step -1] < current_y[x-1]:
            R = -1
        else:
            R = 0

        status = False
        s = step * 488 + (x + 1) * 8 + a + 1
        one_movement(x_coor, a)

        limit_x = min(x+2,60)

        return s, R, status, y_coors[x + 61 * step], y_coors[x + 61 * step - 1], current_y[x], current_y[x+1], 370 - a * 10, y_coors[x + 61 * step], current_y[x+1], current_y[limit_x],pre_y

def get_previous_line():
    search_dir = "/Users/guowei/Downloads/js"
    os.chdir(search_dir)
    files = filter(os.path.isfile, os.listdir(search_dir))
    files = [os.path.join(search_dir, f) for f in files]  # add path to each file
    files.sort(key=lambda x: os.path.getmtime(x))
    new_file = files[-1]
    path = os.path.join(search_dir, new_file)
    f = open(path, 'r')
    # load_dict = js.loads(f.read().encode('utf-8').strip())
    load_dict = js.loads(f.read())
    x = load_dict['paint']['x']
    y = load_dict['paint']['y']
    return len(x), x, y


def calculate_y(length, seq_x, seq_y,):
    previous_y = np.zeros(61)

    for m in range(61):
        if m == 0:
            previous_y[0] = seq_y[0] + 100
        else:
            for i in range(length - 1):
                m1 = 150 + 10 * m
                if m1 > seq_x[i] and m1 <= seq_x[i + 1]:
                    k = (seq_y[i + 1] - seq_y[i]) / (seq_x[i + 1] - seq_x[i])

                    b = seq_y[i + 1] - k * seq_x[i + 1]

                    #print k, b

                    previous_y[m] = k * m1 + b + 100

    return previous_y



# def draw_step(s,a,y_coors):

#     step = int ((s-1)/488)

#     sum = s - step *488

#     x = int((sum-1)/8)

#     y = sum - x*8

#     x_coor = 150 + 10*x

#     y_coor = 370 - 10* (y-1)

#     #x_coors += [x_coor]
#     y_coors += [y_coor]

#     if step == 2 and x == 60 :
#         time.sleep(0.5)
#         pag.press('esc')

#         s = 488*3 +1
#         R = 0
#         status = True
#         return s , R , status, y_coors[182], y_coors[181], y_coors[121], y_coors[121],y_coors[182],y_coors[182],y_coors[121],y_coors[121]


#     elif step == 1 and x == 60 :
#         pag.press('esc')
#         pag.press('p')
#         pag.typewrite('p')
#         time.sleep(2)

#         R = 0
#         status = False

#         s = 488*2 + a+1

#         next_line(a)

#         pag.press('enter')

#         return s, R, status,y_coors[121],y_coors[120],y_coors[60],y_coors[60],y_coors[121],y_coors[121],  y_coors[60],y_coors[60]

#     elif step ==0 and x ==60 :





#         R = 0
#         status = False
#         s =488+a

#         next_line(a)
#         pag.press('enter')
#         return s, R, status, y_coors[60], y_coors[59], 374,374, y_coors[60],y_coors[60],374,374
#         # return s, R, status, y_coors[60], y_coors[59], 370,370, y_coors[60],y_coors[60],370,370

#     elif step ==2 and x ==59 :
                                                                                                                                                           
#         R=3
#         status = False
#         s = 488 +488 +480 + a+1

#         one_movement(x_coor,a)

#         pag.press('esc')
#         pag.press('p')
#         pag.typewrite('p')
#         time.sleep(2)
#         R = readreward2()
#         return s,R,status,y_coors[181],y_coors[180],y_coors[120],y_coors[121],370-a*10 ,y_coors[181] , y_coors[121],y_coors[121]

#     elif step == 1 and x ==59 :
#         R =2
#         status = False
#         s = 488  + 480 + a+1
#         one_movement(x_coor, a)

#         pag.press('esc')
#         pag.press('p')
#         pag.typewrite('p')
#         time.sleep(2)
#         R = readreward()

#         return s,R,status,y_coors[120],y_coors[119],y_coors[59],y_coors[60]  ,  370-a*10 ,y_coors[120] ,y_coors[60],y_coors[60]

#     elif step == 0 and x ==59:


#         status = False

#         s = 480 + a+1

#         one_movement(x_coor, a)
#         pag.press('esc')
#         pag.press('p')
#         pag.typewrite('p')
#         time.sleep(2)


#         R = readreward()
#         return s, R, status , y_coors[59], y_coors[58], 374, 374, 370-a*10, y_coors[59] , 374,374
#         # return s, R, status , y_coors[59], y_coors[58], 370, 370, 370-a*10, y_coors[59] , 370,370

#     elif step ==0 and x == 0 :


#         R = 0
#         status = False
#         s = (x+1)* 8 + a + 1
#         pag.press('enter')



#         one_movement(x_coor, a)
#         return s, R ,status,y_coors[0],y_coors[0],374,374 , 370-a*10, y_coors[0], 374,374

#         # return s, R ,status,y_coors[0],y_coors[0],370,370 , 370-a*10, y_coors[0], 370,370

#     elif x== 0 :

#         R = 0
#         status = False
#         s = step*488 + (x+1) * 8 + a + 1
#         one_movement(x_coor, a)

#         return s, R, status, y_coors[x + 61 * step], y_coors[ x + 61 * step], y_coors[x + 61 * (step - 1)], y_coors[x + 61 * (step - 1) + 1] , 370- a*10,y_coors[ x + 61 * step],y_coors[x + 61 * (step - 1)+1], y_coors[x + 61 * (step - 1) + 2]






#     elif step == 0 :

#         R = 0
#         status = False
#         s= (x+1)* 8 + a+1

#         one_movement(x_coor,a)
#         return s,R, status,y_coors[x], y_coors[x-1],374,374 , 370-a*10, y_coors[x],374,374
#         # return s,R, status,y_coors[x], y_coors[x-1],370,370 , 370-a*10, y_coors[x],370,370

#     else :
#         R = 0

#         status = False
#         s = step * 488 + (x+1 )* 8 + a + 1
#         one_movement(x_coor, a)
#         return s, R, status, y_coors[x + 61 * step],y_coors[ x + 61 * step-1], y_coors[x + 61 * (step - 1)], y_coors[x + 61 * (step - 1) + 1],370 - a*10, y_coors[x + 61 * step], y_coors[x + 61 * (step - 1) + 1],y_coors[min((x +61*(step -1)+2),(step*61 -1))]

#         # return s, R, status, y_coors[x + 61 * step],y_coors[ x + 61 * step-1], y_coors[x + 61 * (step - 1)], y_coors[x + 61 * (step - 1) + 1],370 - a*10, y_coors[x + 61 * step], y_coors[x + 61 * (step - 1) + 1],min((y_coors[x + 61 * (step - 1) + 2]),(step*61 -1))




def readreward():
    search_dir = "/Users/guowei/Downloads/js"
    os.chdir(search_dir)
    files = filter(os.path.isfile, os.listdir(search_dir))
    files = [os.path.join(search_dir, f) for f in files]  # add path to each file
    files.sort(key=lambda x: os.path.getmtime(x))

    time.sleep(1)
    new_file = files[-1]
    path = os.path.join(search_dir, new_file)
    f = open(path, 'r')
    # load_dict = js.loads(f.read().encode('utf-8').strip())
    load_dict = js.loads(f.read())
    reward = load_dict['reward']
    return reward



def readreward2():
    search_dir = "/Users/guowei/Downloads/js"
    os.chdir(search_dir)
    files = filter(os.path.isfile, os.listdir(search_dir))
    files = [os.path.join(search_dir, f) for f in files]  # add path to each file
    files.sort(key=lambda x: os.path.getmtime(x))
    new_file = files[-1]
    path = os.path.join(search_dir, new_file)
    
    f = open(path, 'r')
    # load_dict = js.loads(f.read().encode('utf-8').strip())
    load_dict = js.loads(f.read())
    final_score = load_dict['updated_score']
    time.sleep(1)
    old_file = files[-3]  # second file
    path1 = os.path.join(search_dir, old_file)
    f1 = open(path1, 'r')
    second_score = js.loads(f1.read())['updated_score']
    reward = final_score - second_score
    return reward

def read_grade():
    search_dir = "/Users/guowei/Downloads/js"
    os.chdir(search_dir)
    files = filter(os.path.isfile, os.listdir(search_dir))
    files = [os.path.join(search_dir, f) for f in files]  # add path to each file
    files.sort(key=lambda x: os.path.getmtime(x))
    new_file = files[-1]
    path = os.path.join(search_dir, new_file)
    f = open(path, 'r')
    # load_dict = js.loads(f.read().encode('utf-8').strip())
    load_dict = js.loads(f.read())
    final_score = load_dict['updated_score']
    return final_score