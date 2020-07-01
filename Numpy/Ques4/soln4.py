# Read the variable from STDIN
n = int(input())

import numpy as np
array = np.ones((n,n),dtype=int)
array[1:-1,1:-1]=0
print(array)