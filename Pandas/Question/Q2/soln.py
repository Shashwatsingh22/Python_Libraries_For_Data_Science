import numpy as np
import pandas as pd


df = pd.read_csv('marks_1.csv',sep="|",header=None,index_col=0)
df.index.name = "S.No."
df.columns = ["Name","Subject","Maximum Marks","Marks Obtained","Percentage"]
print(df)