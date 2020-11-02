from math import *
d1 = []
d2 = []
d3 = []

for i in range (11):
	d1 += [i**2]

for j in range (14,26):
	d2 += [sqrt(j)]

for k in range (11):
	d3 += [(d1[k],d2[k])]

print d3	
