# Wesley Smith & Juan Orozco
# Project 6: Random Processes
# Description: Simple simulation of the expansion of a gas (Monte Carlo)

from math import sqrt, exp, factorial
from random import random
import matplotlib.pyplot as plt
import math

# Lists and variables
n = 100 #total number of molecules
nLeft = int(n/2) #number of molecules that are on the left side of the box
time = 0
tList = []
nLeftList = []
hist = []
probabilities = []

# Probability function
def getProbability(nn, nnLeft):
	return (1/(2**nn))*(factorial(nn)/(factorial(nnLeft)*factorial(nn-nnLeft)))

# Add 0s to the hist list
for i in range(n+1):
	hist.append(0)

# Expansion of gas loop
while time < 5000:
	randMolecule = random()*n # choose molecules
	
	#move molecule to other side of box
	if randMolecule < nLeft:
		nLeft -= 1
	else:
		nLeft += 1
		
	hist[nLeft] += 1
		
	# Add items to lists
	tList.append(time)
	nLeftList.append(nLeft)
	time += 1

# Add probabilities to the list
for i in range(n+1):
	probabilities.append(getProbability(n, i)*time)

# Setup graph
plt.plot(range(n+1), probabilities, color="blue", label = "Binomial Distribution")
plt.title("Expansion of Gas")
plt.xlabel("time")
plt.ylabel("probability")
plt.bar(range(n+1), hist, label = "Monte Carlo results")

# Display graph
plt.legend()
plt.show()
