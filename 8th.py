import numpy as np
import pandas as pd

# a=np.array([0,2,1,3,1,1])
# b=np.zeros([a.size,a.max()+1])
# b[np.arange(a.size),a]=1
# print(b)

# a = np.array([0,1,2,3])
# b = np.array((1,2,3,4))
# print(a+b)
# print(np.add(a,b))
# print(np.subtract(a,b))
# print(np.matmul(a,b))

# a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# b = np.array((1,2,0,1))

# c = np.array((a[np.arange(b.size),b]))

# print(c)

data = [[50, True], [40, False], [30, False]]
label_rows = ["Sally", "Mary", "John"]
label_cols = ["age", "qualified"]
df = pd.DataFrame(data, index=label_rows, columns= label_cols) #or
# df = pd.DataFrame(data,label_rows,label_cols)
print(df,"\n")
print(df.loc[["Sally", "John"], ["age", "qualified"]])

# print(df.loc["Mary","age"]) 
# print(df.iloc[[0]])
# info = {'one' : pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),
#  'two' : pd.Series([1, 2, 3, 4, 5, 6, 7, 8], index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])}
# d1 = pd.DataFrame(info)
# print (d1 [['one']])
# print("Add new column")
# d1['three']=pd.Series([20,40,60],index=['a','b','c'])
# print(d1)
# print("Add new column using existing DataFrame columns")
# d1['four']=d1['one']+d1['three']
# print(d1) 
