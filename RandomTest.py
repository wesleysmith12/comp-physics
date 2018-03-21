from math import sqrt, exp, factorial
from random import random
import matplotlib.pyplot as plt

x = []
y = []

for i in range(20):
	print(int(random()))
	
for i in range(50):
	print(int(random()*10))
	
for i in range(1000):
	x.append(random()*10)
	y.append(random()*10)
	
plt.plot(x, y, marker="X", markersize=2, color="blue", linestyle="None")

plt.axis("scaled")
plt.xlim(0,10)
plt.ylim(0,10)
plt.xticks(range(11))
plt.yticks(range(11))
plt.grid()
plt.title("1000 random points")
plt.xlabel("x")
plt.ylabel("y")
	
plt.show()	