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



# display the missing values in the dataframe 

import pandas as pd 

data={
    'Name':["joel","Eliton",None,"Afod"],
    'Age':[20,None,21,22,23],
    'city':["kla","Mkn","Jja",None]
}

df_missing=pd.Dataframe(data)
print(df_missing)

# drop rows with missing values
df_drooped=df_missing.dropna()
print(df_dropped)

#Filling missing values 
df_filled = df_missing.fillna({
    'Name':'Unknown',
    'Age':int(df_missing['Age'].mean()),
    'Salary':0,
    'city':'Kampala'
})
print(df_filled)


#Filtering 
filtered_df=df_missing[df_missing['Age']>22.5]
print(filtered_df)

#data grouping 
#group by city and calculate the mean age of each city 

group_df=df_filled.groupby('City')['Age'].mean()
print(group_df)
