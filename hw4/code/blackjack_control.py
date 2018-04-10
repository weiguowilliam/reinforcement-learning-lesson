import numpy as np
import matplotlib.pyplot as plt

from MCES import MCES
from blackjack_setup import *

initial_Q = np.zeros([200,2])
initial_policy = np.ones([200, 2]) / 2
gamma = 1
alpha = 0

num_episodes = 100000
Q,_ = MCES(get_episode_blackjack,initial_Q,initial_policy,gamma,alpha,num_episodes)
optimal_actions = Q.argmax(axis=1)

action_noUsableAce = optimal_actions[:100].reshape(10,10,order='F')
action_noUsableAce = np.append(np.zeros([1,10]), action_noUsableAce,axis=0)

action_usableAce = optimal_actions[100:].reshape(10,10,order='F')
action_usableAce = np.append(np.zeros([1,10]),action_usableAce,axis=0)


def plot_actions(actions,title_str):
    fig,ax = plt.subplots()
    ax_ = ax.imshow(actions,interpolation='nearest',
                            origin='lower',cmap='gray',alpha=0.8)
    cbar = fig.colorbar(ax_,ticks=[0,1])
    cbar.ax.set_yticklabels(['hit','stand'])
    ax.set_title(title_str)
    ax.set_xlabel('Dealer showing')
    ax.set_ylabel('Player sum')
    ax.xaxis.set_ticks(np.arange(10))
    ax.xaxis.set_ticklabels(['A',2,3,4,5,6,7,8,9,10])
    ax.yaxis.set_ticks(np.arange(11))
    ax.yaxis.set_ticklabels(np.arange(11,22))
#   fig.savefig(title_str+'.jpg',dpi=200)

plot_actions(action_usableAce, 'Usable ace')
plot_actions(action_noUsableAce,'No usable ace')
plt.show()
true_action_usableAce = np.zeros([11,10])
true_action_usableAce[-4:] = 1
true_action_usableAce[-4][[0,8,9]] = 0

true_action_noUsableAce = np.ones([11,10])
true_action_noUsableAce[:6,0] = 0
true_action_noUsableAce[:2,1:3] = 0
true_action_noUsableAce[0,3:6] = 0
true_action_noUsableAce[:6,-4:]=0

diff_usableAce = np.sum(action_usableAce != true_action_usableAce)
diff_noUsableAce = np.sum(action_noUsableAce != true_action_noUsableAce)
error_rate = (diff_usableAce + diff_noUsableAce)/200
print('Number of states that have non-optimal action: ', diff_usableAce + diff_noUsableAce)
print('Error rate: ', error_rate)

