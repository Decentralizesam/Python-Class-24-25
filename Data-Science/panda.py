import pandas as pd 
data={
    'Name':['elton','samson','yasin'],
    'Age':[20,21,22],
    'course':['python','java','sql']
}
df=pd.DataFrame(data)

print(df.head())


df1=pd.read_json('datasets/users.json')


#Data cleaning 
# it involves handling missing values ,removing duplicates and correcting data types


#checking for the missing values 
#isnull function identidies missing values
print(df.isnull().sum())
#filling missing values with the mean of the columns 
#df['value'].fillna(df['value'].mean())

#Basic statistics of a data set
print(df.describe()) #NB: this describes the data 

data1={'Name':['james','Duke'],
       'Age':[20,21],
}

data2={'Name':['june','job'],
'Age':[6,6]
}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

#merged based on common columns 
merged_df=pd.merge(df1,df2,on='Name',how='inner')
#print(merged_df)

#calculation
mean.age=df['Age'].mean()
print(mean_age)





import pandas as pd 

data={
    'Name':["joel","Eliton",None,"Afod"],
    'Age':[20,None,21,22,23],
    'city':["kla","Mkn","Jja",None]
}
