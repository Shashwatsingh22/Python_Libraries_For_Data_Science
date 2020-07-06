# Read the variable from STDIN
n = int(input())

import numpy as np 
import pandas as pd 

num_list=np.arange(1,n+1)

ds = pd.Series(num_list**2,index=num_list)
print(num_list)
print(ds)