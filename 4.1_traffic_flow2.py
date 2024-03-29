#!/usr/bin/env python
# coding: utf-8

# In[179]:


import numpy as np


# In[360]:


class TrafficSimulation():
    #initialization accepts (road length, traffic density, maximum velocity, probability of slowing down)
    def __init__(self, length,t_density,v_max,p_slow,in_v=0):
        self.length=length
        self.t_density=t_density
        self.v_max=v_max
        self.p_slow=p_slow
        self.in_v=in_v
        self.c_state=np.full((self.length),-1,dtype=int) #a np array full of -1's
        self.n_state=np.full((self.length),-1,dtype=int) #a np array full of -1's for next state
    
    def start(self):
        self.cars=int(self.length*self.t_density) #getting the number of cars based on length and density 
        self.a=np.random.choice(self.length,self.cars,replace=False) #getting the random indexes where we 
        #will place the cars at the beginning 
        for i in range(self.cars): #adding cars with initial velocity v=0 at those random places 
            self.c_state[self.a[i]]=self.in_v   
    

    def update(self): 
        for i in range(self.length): #iterating through the 1D array
            if self.c_state[i]!=-1: #check if there is a car there 
                #print('there is a car in',i,'with velocity=',self.c_state[i])
                spaces=self.check_ahead(i) #checking the number of spaces ahead
                #print('there are',spaces,'spaces till the next car')
                if spaces>(self.c_state[i]+1) and self.c_state[i]<self.v_max: 
                    #if number of free spaces is greater than current velocity +1
                    self.c_state[i]+=1 #accelerate
                    #print('acceleration, new velocity is',self.c_state[i])
                elif spaces<=self.c_state[i]: #if there is a car at a space index less or = than v
                    if self.c_state[i]==0:
                        self.c_state[i]=0
                    else:
                        self.c_state[i]=spaces-1 #slow down 
                    #print('slowing down, new velocity is',self.c_state[i])
                if self.c_state[i]>0: #reducing the speed of every car by 1 with probability p 
                    if np.random.random()<self.p_slow: 
                        self.c_state[i]-=1
                        #print('car ',i,'was slowed down. new v is:',self.c_state[i])
        for i in range(self.length): #moving all cars v spaces
            if self.c_state[i]!=-1:
                #print('there is a car in',i,'with v',self.c_state[i])
                self.n_state[(i+self.c_state[i])%self.length]=self.c_state[i]
                #print('car in',i,'moved',self.c_state[i],'spaces. new index is',(i+self.c_state[i])%self.length)
                #self.n_state[i - velocity]=velocity
        self.c_state=self.n_state #updating current state
        
        self.n_state=np.full((self.length),-1,dtype=int) #a np array full of -1's for next state
    

    def check_ahead(self,i): #receives the index of the car and its current velocity
        free_spaces=0 #starts a counter for the number of empty spaces
        for s in range(1,self.v_max+2):
            if self.c_state[(i+s)%self.length]==-1:
                free_spaces+=1
            else: 
                break
        return free_spaces
    
    def display(self):
        print(''.join('.' if c==-1 else str(c) for c in self.c_state))

    def run(self):
        self.start()
        self.display()
        for r in range(40):
            self.update()
            self.display()


# In[361]:


my_sim1=TrafficSimulation(length=100,t_density=0.03,v_max=5,p_slow=0.5)
my_sim1.run()


# In[362]:


my_sim2=TrafficSimulation(length=100,t_density=0.1,v_max=5,p_slow=0.5)
my_sim2.run()


# In[ ]:





# In[ ]:




