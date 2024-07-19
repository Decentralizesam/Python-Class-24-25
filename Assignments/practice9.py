import pandas as pd
import json

with open('Data-Science/datasets/users.json', 'r') as file:
    data = json.load(file)

df = pd.DataFrame(data)

# Inspect Data
print(df.head())
print(df.info())
print(df.describe())

# Handle Missing Values
df.fillna({'id': 'name', 'age': 0, 'city': 'friends'}, inplace=True)

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Data Type Conversion (if needed)
df['age'] = df['age'].astype('int')

# Save Cleaned Data
df.to_json('cleaned_users.json', orient='records', lines=True)