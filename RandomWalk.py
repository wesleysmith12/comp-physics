# Wesley Smith & Juan Orozco
# Project 6: Random Processes
# Description: Random walks

from math import sqrt, exp, factorial
from random import random
import matplotlib.pyplot as plt
import math

x = 0 # Current x position
xList = [] # list of the x position
time = 0 # Current time
rand = 0 # Random var for 50%
iterationsSteps = 1000
walkers = 20 # Repeat the simulation several times over
sumOfW = 0

# Simulate random walks
for i in range(walkers):
    x = 0
    xList = []

    for j in range(iterationsSteps):
        rand = int(random()*2)# 50%

        if(rand > 0):
            x += 1
        else:
            x -= 1

        time += 1
        xList.append(x)
    sumOfW += x**2
    plt.plot(range(iterationsSteps), xList)
rms = sqrt(sumOfW/walkers)

# Setup graph
print("RMS: ",rms)
plt.title("Random walks: Postion V.S Time")
plt.xlabel("Time")
plt.ylabel("X Postion")
plt.show()


