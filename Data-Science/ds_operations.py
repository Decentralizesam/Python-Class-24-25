import pandas as pd
import numpy as np
import json

bands_df=pd.read_csv('datasets/bands-csv.csv')

#load the json data 
with open('datasets/users.json')as f:
    users_data=json.load(f)
users_df=pd.json_normalize(users_data)

# filling in the missing fields
bands_df.fillna({
    'year':'2006',
    'industry_name_ANZSIC':"Undefined Industry",
    'Value':0

},inplace=True)

#print('Bands Dataframe:')
#print(bands_df.head())

#print('\nUsers Dataframe:')
#print(users_df.head())

#converting string column to intergers
users_df["id"]=users_df["id"].astype(int)
users_df["age"]=users_df["age"].astype(int)


print("/Cleaned Bands Dataframe:")
print(bands_df.head())

print("/Cleaned Bands Dataframe:")
print(users_df.head())

# Basic Analysis Pandas
user_age_count = users_df['city'].value_counts()
print(user_age_count)

# mean age of users 
user_age_average = users_df['age'].mean().astype(int)
print(f"/n the average age of users is :{user_age_average}")

# Basic transformation methods with numpy 
#Creating a numpy array from a data frame column with is 'age'

ages=users_df['age'].to_numpy()
mean_age=np.mean(ages)
std_age=np.std(ages)

normalized_age=(ages-mean_age)/std_age


print(normalized_age[:10])# Displays the first 10 normalized ages 
print(f"/n the average age of users is :{mean_age} \n The standard deviation of age:{std_age}")

#Advanced data transformation 
current_year=pd.Timestamp.now().year
bands_df['value']=current_year - bands_df['year'].astype(int)

# catergorize users into age group 
def age_group(age):
    if age<20:
        return "teen"
    elif 20 <=age < 30:
        return "young adult"

    elif 30 <=age < 50:
        return "young adult"
    else:
        return "senior"

users_df['age_group']=users_df['age'].apply(age_group)
print("\n users dataframe with group")
print(users_df.head)



#Sample Dataframe with categories 
data={
    'ID':[1,2,3,4,5,6,7],
    'categories':['A','B','C','A','B','C','A']
}

df=pd.DataFrame(data)
#Define mapping of categories to intergers
category_mapping={'A':1,'B':2,'C':3}
df['Categories']=df['Categories'].map(category_mapping)
print('Dataframe after Mapping')
print(df)
