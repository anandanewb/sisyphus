# Ex 26  Celebrity Deaths
import pandas as pd
import numpy as np

cols = ['dateofdeath', 'age']

df = pd.read_csv('data/celebrity_deaths_2016.csv', usecols=cols)

df['dateofdeath'] = pd.to_datetime(df['dateofdeath'])
df['monthofdeath'] = df['dateofdeath'].dt.month
df.set_index(df.monthofdeath, inplace=True)
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df = df.loc[df.age < 120]
df = df.sort_index()
df.loc[2:7, 'age'].mean()
df['dayofdeath'] = df.dateofdeath.dt.day
df = df.set_index(['monthofdeath', 'dayofdeath'])
df = df.sort_index()

#average age of death from Feb 15 - July 15
df.loc[(2,15):(7,15), 'age'].mean()
df.loc[(2,15):(7,15)]

cols = cols + ['causeofdeath']

df2 = pd.read_csv('data/celebrity_deaths_2016.csv', usecols=cols)
df2 = df2.fillna('Unknown')
