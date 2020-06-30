#take input here
import ast 
input_list=ast.literal_eval(input())
m=int(input())
n=int(input())

import numpy as np
array_1 =np.array(input_list)
array_1=array_1[array_1>m]
final_array=array_1[array_1<n]#start writing your code from here
 #start writing your code from here

print(final_array)

