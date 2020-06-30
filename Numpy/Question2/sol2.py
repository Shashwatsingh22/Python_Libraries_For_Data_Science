# Read the input list
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)

import numpy as np

# Convert the input list to a NumPy array
array_2d =np.array(input_list)

# Extract the first column, first row, last column and last row respectively using
# appropriate indexing
col_first = array_2d[:,0]
print(col_first)
row_first = array_2d[0]
print(row_first)
size=array_2d.shape
row=size[0]
col=size[1]
col_last = array_2d[:,col-1]
print(col_last)
row_last = array_2d[row-1]
print(row_last)