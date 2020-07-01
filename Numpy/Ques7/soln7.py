# Read the input
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
list_1 = input_list[0]
list_2 = input_list[1]
list_3 = input_list[2]

# Import NumPy
import numpy as np
x=np.array(list_1)
y=np.array(list_2)
z=np.transpose(np.array(list_3))

t=np.vstack((x,y))

final_array=np.hstack((t,z))

# Write your code here
print(final_array)
