
# coding: utf-8
# Wei Guo(wg8we)

## Question 7 

# In[2]:

import random
random.seed(1)


# In[44]:

class Student(object):
    y = 1 # y is discounting rate
    
    def __init__(self):
        self.s = "class1"
        self.r = -2
        self.end = False
        self.reset()
        
    def step(self):
        """
        one step of student from one state(s) to another state
        """
        if self.s == "class1":
            if random.random()<=0.5:
                self.s = "class2"
                self.r += -2
            else:
                self.s = "facebook"
                self.r += -1
        elif self.s == "facebook":
            if random.random()<=0.9:
                self.s= "facebook"
                self.r += -1
            else:
                self.s = "class1"
                self.r += -2
        elif self.s == "class2":
            if random.random()<=0.9:
                self.s = "class3"
                self.r += -2
            else:
                self.s = "sleep"
                self.r += 0
                self.end = True
        elif self.s == "class3":
            if random.random()<=0.6:
                self.s = "pass"
                self.r += 10
            else:
                self.s = "pub"
                self.r += 1
        elif self.s == "pub":
            if random.random()<=0.4:
                self.s = "class3"
                self.r += -2
            elif (random.random()>0.4) and (random.random()<=0.8):
                self.s = "class2"
                self.r += -2
            else:
                self.s = "class1"
                self.r += -2
        elif self.s == "pass":
            self.s = "sleep"
            self.r += 0
            self.end = True
        elif self.s == "sleep":
            self.end = True
        else:
            raise Exception("ERROR: Undefined transition!")
            
    def reset(self):
        """
        reset the mrp
        """
        self.s = "class1"
        self.r = -2


# In[52]:

def episode(s):
    while s.end==False:
        print("the state is "+ s.s)
        print("the return now is " + str(s.r))
        s.step()
    print("The final return is "+str(s.r))
    

# while(s1.end==False):
#     print(s1.s)
#     s1.step()

# print(s1.r)


# In[ ]:

s1 = Student();
episode(s1)

# the first episode is
# the state is class1
# the return now is -2
# the state is class2
# the return now is -4
# the state is class3
# the return now is -6
# the state is pub
# the return now is -5
# the state is class3
# the return now is -7
# the state is pass
# the return now is 3
# The final return is 3

# In[ ]:

s2 = Student();
episode(s2)
# the seconde episode is
# the state is class1
# the return now is -2
# the state is class2
# the return now is -4
# the state is class3
# the return now is -6
# the state is pub
# the return now is -5
# the state is class3
# the return now is -7
# the state is pass
# the return now is 3
# The final return is 3

# In[ ]:

s3 = Student();
episode(s3)
#the third episode is
# the state is class1
# the return now is -2
# the state is facebook
# the return now is -3
# the state is facebook
# the return now is -4
# the state is facebook
# the return now is -5
# the state is facebook
# the return now is -6
# the state is facebook
# the return now is -7
# the state is facebook
# the return now is -8
# the state is facebook
# the return now is -9
# the state is class1
# the return now is -11
# the state is facebook
# the return now is -12
# the state is facebook
# the return now is -13
# the state is facebook
# the return now is -14
# the state is facebook
# the return now is -15
# the state is class1
# the return now is -17
# the state is class2
# the return now is -19
# the state is class3
# the return now is -21
# the state is pass
# the return now is -11
# The final return is -11


# # Question 8

# In[57]:

import random
random.seed(1)


# In[58]:

class Student2(object):
    y = 1 # y is discounting rate
    
    def __init__(self):
        self.s = "class1"
        self.r = 0
        self.a = None
        self.end = False
        self.reset()
        
    def step(self):
        """
        one step of student from one state(s) to another state
        """
        if self.s == "class1":
            if random.random()<=0.5:
                self.a = "study"
                self.s = "class2"
                self.r += -2
            else:
                self.a = "relax"
                self.s = "facebook"
                self.r += -1
        elif self.s == "facebook":
            if random.random()<=0.5:
                self.a = "relax"
                self.s= "facebook"
                self.r += -1
            else:
                self.a = "study"
                self.s = "class1"
                self.r += 0
        elif self.s == "class2":
            if random.random()<=0.5:
                self.a = "study"
                self.s = "class3"
                self.r += -2
            else:
                self.a = "relax"
                self.s = "sleep"
                self.r += 0
                self.end = True
        elif self.s == "class3":
            if random.random()<=0.5:
                self.a = "study"
                self.s = "pass"
                self.r += 10
            else:
                self.a = "relax"
                self.r += 1
                if random.random()<=0.4:
                    self.s = "class3"
                elif (random.random()>0.4) and (random.random()<=0.8):
                    self.s = "class2"
                else:
                    self.s = "class1"
        elif self.s == "sleep":
            self.end = True
        else:
            raise Exception("ERROR: Undefined transition!")
            
    def reset(self):
        """
        reset the mrp
        """
        self.s = "class1"
        self.r = 0
        self.a = None
        self.end = False


# In[62]:

def episode2(s):
    while s.end==False:
        print("the state is "+ s.s)
        s.step()
        print("the action is " + s.a)
        print("the return now is " + str(s.r))
        
    print("The final return is "+str(s.r))


# In[ ]:

s4 = Student2()
episode2(s4)
# the first episode is 
# the state is class1
# the action is study
# the return now is -2
# the state is class2
# the action is relax
# the return now is -2
# The final return is -2

# In[ ]:

s5 = Student2()
episode2(s5)
#the second episode is
# the state is class1
# the action is study
# the return now is -2
# the state is class2
# the action is study
# the return now is -4
# the state is class3
# the action is relax
# the return now is -3
# the state is class3
# the action is relax
# the return now is -2
# the state is class1
# the action is study
# the return now is -4
# the state is class2
# the action is relax
# the return now is -4
# The final return is -4

# In[ ]:

s6 = Student2()
episode2(s6)
# the third episode is
# the state is class1
# the action is relax
# the return now is -1
# the state is facebook
# the action is study
# the return now is -1
# the state is class1
# the action is relax
# the return now is -2
# the state is facebook
# the action is relax
# the return now is -3
# the state is facebook
# the action is relax
# the return now is -4
# the state is facebook
# the action is relax
# the return now is -5
# the state is facebook
# the action is relax
# the return now is -6
# the state is facebook
# the action is study
# the return now is -6
# the state is class1
# the action is relax
# the return now is -7
# the state is facebook
# the action is study
# the return now is -7
# the state is class1
# the action is relax
# the return now is -8
# the state is facebook
# the action is study
# the return now is -8
# the state is class1
# the action is study
# the return now is -10
# the state is class2
# the action is relax
# the return now is -10
# The final return is -10


# # Oil Lease Problem

# The policy is to pump with enhanced pressure when price is 30, to pump normally when price is 20 and never wait.
# 
# I ll run the episode for 10000 times and get the average return. This return will be the lease price.

# In[68]:

import random
random.seed(1)


# In[69]:

class Oil(object):
    
    def __init__(self):
        self.s = 100 # s for storage of oil, not for state
        self.state = "year0" # state for state space for problem
        self.r = 0 # return
        self.a = "start" # a for action for object
        self.end = False
        self.reset()
    
    def step(self):
        if self.state == "year0":
            if random.random()<=0.5: # P(price=20)=0.5
                self.a = "normal pump"
                self.r +=self.s*0.2*20 #pump*price
                self.s = self.s*0.8
                self.state = "year1"
            else: #price = 30
                self.a = "enhanced pump"
                self.r += self.s*0.36*30
                self.s = self.s*0.64
                self.state = "year1"
        elif self.state == "year1":
            if random.random()<=0.5: #price=20
                self.a = "normal pump"
                self.r +=self.s*0.2*20
                self.s = self.s*0.8
                self.state = "year2"
            else:
                self.a = "enhanced pump"
                self.r += self.s*0.36*30
                self.s = self.s*0.64
                self.state = "year2"
        elif self.state == "year2":
            if random.random()<=0.5: #price=20
                self.a = "normal pump"
                self.r +=self.s*0.2*20
                self.s = self.s*0.8
                self.state = "year3"
                self.end = True
            else:
                self.a = "enhanced pump"
                self.r += self.s*0.36*30
                self.s = self.s*0.64
                self.state = "year3"
                self.end = True
        
    def reset(self):
        """
        reset the episode
        """
        self.s = 100 # s for storage of oil, not for state
        self.state = "year0" # state for state space for problem
        self.r = 0 # return
        self.a = "start" # a for action for object
        self.end = False


# In[70]:

def episode3(s):
    while s.end==False:
#         print("the state is "+ s.state)
        s.step()
#         print("the action is " + s.a)
#         print("the storage now is " + str(s.s))
#         print("the return now is " + str(s.r))
        
#     print("The final return is "+str(s.r))
    return s.r


# In[71]:

# test for one episode
s = Oil()
episode3(s)


# In[76]:

# run simulation for 1000 times
n = 10000
l = [0]
for i in range(n):
    s = Oil()
    l.append(episode3(s))


# In[77]:

price = sum(l) / float(len(l))
print("the price of lease is "+str(price))
#the price of lease is 1655.65247635245.



