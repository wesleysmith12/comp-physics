# Wesley Smith & Juan Orozco
# Project 6: Random Processes
# Description: Simulate the nuclear decay experiment 
# may times.

from math import sqrt, exp, factorial
from random import random
import matplotlib.pyplot as plt
import math

n = 10000 # Starting number
count = 0 # Counter to do 100 initial simulations
countMax = 100 # The max number of simulations
number = 0 # Random number
occurrences = [] # Occurrences list
xRange = 30 # X range on the graph
pList = [] # The poisson list

# The poisson probability distribution function
def poisson(k,lambdaV):
    return (1/factorial(k))*(lambdaV**k)*(math.e**(-lambdaV))

# Calculate the poisson probability distribution
for i in range(xRange):
    pList.append(poisson(i,10)*countMax)

# Setup occurrences list
for i in range(xRange):
    occurrences.append(0)

# Carry out nuclear decay simulation many times
while(count < countMax):
    n = 10000
    for i in range(n):
        number = int(random()*1000) # .001 probability
        if(number == 1):
            n -= 1
    occurrences[10000-n] += 1
    count += 1

# Plot the graphs
plt.plot(range(xRange), pList, color="red", label="Poisson distribution")
plt.title("Nuclear decay")
plt.xlabel("Number of decays")
plt.ylabel("Number of occurrences")
plt.bar(range(xRange), occurrences, color="blue", label="Simulation")
plt.legend()
plt.show()
