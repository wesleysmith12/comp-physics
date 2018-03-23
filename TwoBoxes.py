from math import sqrt, exp, factorial
from random import random
import matplotlib.pyplot as plt
import math

n = 100 #total number of molecules
nLeft = int(n/2) #number of molecules that are on the left side of the box
time = 0
tList = []
nLeftList = []
hist = []
probabilities = []

def getProbability(nn, nnLeft):
	return (1/(2**nn))*(factorial(nn)/(factorial(nnLeft)*factorial(nn-nnLeft)))

for i in range(n+1):
	hist.append(0)

while time < 5000:
	randMolecule = random()*n # choose molecules
	
	#move molecule to other side of box
	if randMolecule < nLeft:
		nLeft -= 1
	else:
		nLeft += 1
		
	hist[nLeft] += 1
		
	tList.append(time)
	nLeftList.append(nLeft)
	#probabilities.append(getProbability()*time)
	time += 1

	
#plt.plot(tList, nLeftList, marker="X", markersize=2, color="blue")
#plt.ylim(0,n)
#plt.grid()
#plt.title("Expansion of Gas")
#plt.xlabel("Time")
#plt.ylabel("Remaining molecules on left")

for i in range(n+1):
	probabilities.append(getProbability(n, i)*time)

plt.plot(range(n+1), probabilities, color="blue", label = "Binomial Distribution")
plt.title("Expansion of Gas")
plt.xlabel("time")
plt.ylabel("probability")

#probability = (1/(2**n))*(factorial(n)/(factorial(nLeft)*factorial(n-nLeft)))

plt.bar(range(n+1), hist, label = "Monte Carlo results")

#plt.title("Expansion of Gas")
#plt.xlabel("nLeft")
#plt.ylabel("nleft occurances")

plt.legend()
plt.show()
