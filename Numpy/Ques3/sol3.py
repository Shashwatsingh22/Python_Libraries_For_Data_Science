# Read the variable from STDIN
import numpy as np
n = int(input())
x=np.zeros((2,2),dtype=int)
x[0,1]=1
x[1,0]=1
n=int(n/2)
rep=(n,n)

y=np.tile(x,rep)
print(y)