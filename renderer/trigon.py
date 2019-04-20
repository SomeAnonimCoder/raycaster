import math
RAY_NUM=10000
fov=3.14159/2

sins = []
coss = []
i=0
d=fov/RAY_NUM
while(i<3.1416*2):
	sins.append(math.sin(i))
	coss.append(math.cos(i))
	i+=d;



def sin(x):
	return sins[int(x/d)]


def cos(x):
	return coss[int(x/d)]



