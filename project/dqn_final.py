import random
import numpy as np
import math
import time
import pyautogui as pag
import glob
import os
import tensorflow as tf
from collections import deque

###############################
### NN-code-zhihu ##############
################################

# Hyper Parameters for DQN
GAMMA = 0.9 # discount factor for target Q
INITIAL_EPSILON = 0.5 # starting value of epsilon
FINAL_EPSILON = 0.01 # final value of epsilon
REPLAY_SIZE = 30 # experience replay buffer size
BATCH_SIZE = 10 # size of minibatch

class DQN():
  # DQN Agent
    def __init__(self):
    # init experience replay
        self.replay_buffer = deque()
    # init some parameters
        self.time_step = 0
        self.epsilon = INITIAL_EPSILON
        self.state_dim = 4
#         self.state_dim = env.observation_space.shape[0]
        self.action_dim = 8

        self.create_Q_network()
        self.create_training_method()

    # Init session
        self.session = tf.InteractiveSession()
        self.session.run(tf.global_variables_initializer())

    # loading networks
        self.saver = tf.train.Saver()
        checkpoint = tf.train.get_checkpoint_state("saved_networks")
        if checkpoint and checkpoint.model_checkpoint_path:
        		self.saver.restore(self.session, checkpoint.model_checkpoint_path)
        		print("Successfully loaded:", checkpoint.model_checkpoint_path)
                
        else:
        		print("Could not find old network weights")

        # global summary_writer
        # summary_writer = tf.train.SummaryWriter('~/logs',graph=self.session.graph)

    
    def create_Q_network(self):

     #initial network weights
        W1 = self.weight_variable([4, 8])
        b1 = self.bias_variable([8])
        W2 = self.weight_variable([8,12])
        b2 = self.bias_variable([12])
        W3 = self.weight_variable([12,self.action_dim])
        b3 = self.bias_variable([self.action_dim])

     #input layer
        self.state_input = tf.placeholder('float',[None, 4])

     #hidden layers
        h1 = tf.nn.relu(tf.matmul(self.state_input, W1) + b1)
        h2 = tf.nn.relu(tf.matmul(h1, W2) + b2)

     #Q Value layer
        self.Q_value = tf.matmul(h2, W3) + b3
    
    # def create_Q_network(self):

    # #initial network weights
    #     W1 = self.weight_variable([4, 8])
    #     b1 = self.bias_variable([8])
    #     W2 = self.weight_variable([8,10])
    #     b2 = self.bias_variable([10])
    #     W3 = self.weight_variable([10,12])
    #     b3 = self.bias_variable([12])
    #     W4 = self.weight_variable([12,self.action_dim])
    #     b4 = self.bias_variable([self.action_dim])

    # #input layer
    #     self.state_input = tf.placeholder('float',[None, 4])

    # #hidden layer 1
    #     h1 = tf.nn.relu(tf.matmul(self.state_input, W1) + b1)
    #     h2 = tf.nn.relu(tf.matmul(h1,W2)+b2)
    #     h3 = tf.nn.relu(tf.matmul(h2,W3)+b3)


    # #Q Value layer
    #     self.Q_value = tf.matmul(h3, W4) + b4



    def create_training_method(self):
        self.action_input = tf.placeholder("float",[None,8]) # one hot presentation
        self.y_input = tf.placeholder("float",[None])
        Q_action = tf.reduce_sum(tf.multiply(self.Q_value,8),reduction_indices = 1)
        # Q_action = tf.reduce_sum(self.Q_value[int(self.action_input - 1)])
        self.cost = tf.reduce_mean(tf.square(self.y_input - Q_action))
        self.optimizer = tf.train.AdamOptimizer(0.0001).minimize(self.cost)

    def perceive(self,state,action,reward,next_state,done):
        one_hot_action = np.zeros(self.action_dim)
        # one_hot_action = list(np.zeros(self.action_dim))
        
        one_hot_action[action-1] = 1
        self.replay_buffer.append((state,one_hot_action,reward,next_state,done))
        if len(self.replay_buffer) > REPLAY_SIZE:
            self.replay_buffer.popleft()

        if len(self.replay_buffer) > BATCH_SIZE:
            self.train_Q_network()

    def train_Q_network(self):
        self.time_step += 1
    # Step 1: obtain random minibatch from replay memory
        minibatch = random.sample(list(self.replay_buffer),BATCH_SIZE)
        state_batch = [data[0] for data in minibatch]
        action_batch = [data[1] for data in minibatch]
        reward_batch = [data[2] for data in minibatch]
        next_state_batch = [data[3] for data in minibatch]

    # Step 2: calculate y
        y_batch = []
        Q_value_batch = self.Q_value.eval(feed_dict={self.state_input:next_state_batch})
        for i in range(0,BATCH_SIZE):
            done = minibatch[i][4]
            if done:
                y_batch.append(reward_batch[i])
            else :
                y_batch.append(reward_batch[i] + GAMMA * np.max(Q_value_batch[i]))

        self.optimizer.run(feed_dict={
              self.y_input:y_batch,
              self.action_input:action_batch,
              self.state_input:state_batch})
        
        # save network every 1000 iteration
        if self.time_step % 100 == 0:
            self.saver.save(self.session, 'saved_networks/' + 'network' + '-dqn', global_step = self.time_step)


    def egreedy_action(self,state):
        Q_value = self.Q_value.eval(feed_dict = {self.state_input:[state]})[0]
        if random.random() <= self.epsilon:
            return random.randint(0,self.action_dim - 1)
        else:
            return np.argmax(Q_value)

        self.epsilon -= (INITIAL_EPSILON - FINAL_EPSILON)/10000
        # self.epsilon -= (INITIAL_EPSILON - FINAL_EPSILON)/100
    

    def action(self,state):
        return np.argmax(self.Q_value.eval(feed_dict = {self.state_input:[state]})[0])
        # return np.argmax(self.Q_value.eval(feed_dict = {self.state_input:[state]})[0]),self.Q_value.eval(feed_dict = {self.state_input:[state]})[0]

    def weight_variable(self,shape):
        initial = tf.truncated_normal(shape)
        return tf.Variable(initial)

    def bias_variable(self,shape):
        initial = tf.constant(0.01, shape = shape)
        return tf.Variable(initial)

