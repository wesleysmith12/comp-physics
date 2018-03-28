from math import sqrt, exp, factorial
from random import random
import matplotlib.pyplot as plt
import math

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
number = 0
occurances = []

for i in range(50):
    occurances.append(0)

while(count < 100):
    n = 10000
    for i in range(n):
        number = int(random()*1000)
        if(number == 1):
            n -= 1
    occurances[10000-n] += 1
    count += 1
print(number)
print("n is",n)
plt.bar(range(50), occurances)
# plt.plot(range(t), nList)
#plt.ylim(9950,10000)

#plt.grid()
plt.show()
