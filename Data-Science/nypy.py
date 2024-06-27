import pandas as pd 
import numpy as np 

data=np.array([[2,3,5],[0,2,4]])

#create a dataframe 
df=pd.DataFrame(data,columns=['A','B','C'])
print(df)

