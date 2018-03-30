from math import sqrt, exp, factorial
from random import random
import matplotlib.pyplot as plt
import math

n = 10000
count = 0 # Counter to do 100 initial simulations
number = 0 # Random number
occurances = []# Occurances list
xRange = 30 # X range on the graph
pList = []

def poisson(k,lambdaV):
    return (1/factorial(k))*(lambdaV**k)*(math.e**(-lambdaV))

for i in range(xRange):
    pList.append(poisson(i,10)*100)

for i in range(xRange):
    occurances.append(0)

while(count < 100):
    n = 10000
    for i in range(n):
        number = int(random()*1000) # .001 probability
        if(number == 1):
            n -= 1
    occurances[10000-n] += 1
    count += 1
print(number)
print("n is",n)
plt.plot(range(xRange), pList, color="red", label="Poisson dist")
plt.title("Expansion of Gas")
plt.xlabel("time")
plt.ylabel("probability")
plt.bar(range(xRange), occurances, color="blue", label="Simulation")
plt.legend()
plt.show()
