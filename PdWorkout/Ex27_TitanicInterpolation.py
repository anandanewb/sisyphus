import pandas as pd

#read titanic dataset
df = pd.read_excel('data/titanic3.xls')

null_columns = df.columns[df.isnull().any()]
df['age'] = df['age'].fillna(df['age'].median())

df.isnull().sum()
df = df.dropna(subset=['embarked', 'fare'])

# df['home.dest'] = df['home.dest'].fillna(df['home.dest'].mode()[0])
df2 = df.set_index(['embarked', 'home.dest'])

#find most common home.dest per embarked value
df2 = df2.reset_index()
df2 = df2.groupby('embarked')['home.dest'].agg(lambda x: x.value_counts().index[0])

df['home.dest'] = df['home.dest'].fillna(df['embarked'])

