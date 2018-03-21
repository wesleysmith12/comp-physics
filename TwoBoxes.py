from math import sqrt, exp, factorial
from random import random
import matplotlib.pyplot as plt

n = 1000 #total number of molecules
nLeft = int(n/2) #number of molecules that are on the left side of the box
time = 0
tList = []
nLeftList = []
hist = []

for i in range(n+1):
	hist.append(0)

while time < n:
	randMolecule = random()*n # choose molecules
	
	#move molecule to other side of box
	if randMolecule < nLeft:
		nLeft -= 1
	else:
		nLeft += 1
		
	hist[nLeft] += 1
		
	tList.append(time)
	nLeftList.append(nLeft)
	time += 1

	
plt.bar(tList, nLeftList, marker="X", markersize=2, color="blue")
plt.ylim(0,n)
plt.grid()
plt.title("Expansion of Gas")
plt.xlabel("Time")
plt.ylabel("Remaining molecules on left")

plt.show()
