from math import sqrt, exp, factorial
from random import random
import matplotlib.pyplot as plt
import math

n = 10000
start = n
probability = .001
t = 0
currentProb = 0
count = 0
nList = []
while(n >= 1000):
    for i in range(n):
        number = int(random()*1000)
        if(number == 1):
            n -= 1
    nList.append(n)
    t += 1
print(number)
print("n is",n)
plt.plot(range(t), nList)
plt.ylim(0,10000)

plt.grid()
plt.show()
