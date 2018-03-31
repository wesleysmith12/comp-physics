# Wesley Smith & Juan Orozco
# Project 6: Random Processes
# Description: Simulate nuclear decay

from math import sqrt, exp, factorial
from random import random
import matplotlib.pyplot as plt
import math

n = 10000 # Starting number, this number changes over time
t = 0 # Time step 
nList = [] # Number list

# Carry out nuclear decay simulation
while(n >= 1000):
    for i in range(n):
        number = int(random()*1000)# choose a number from 1000
        if(number == 1):# .001 probability
            n -= 1
    nList.append(n)
    t += 1

# Plot graph
plt.plot(range(t), nList)
plt.ylim(0,10000)
plt.grid()
plt.show()
