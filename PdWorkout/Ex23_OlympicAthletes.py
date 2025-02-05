import pandas as pd
import numpy as np
from pandas import IndexSlice as idx

cols = ['Age', 'Height', 'Team', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal']
index_cols = ['Year', 'Season', 'Sport', 'Event']
df = pd.read_csv('data/olympic_athlete_events.csv', usecols=cols, index_col=index_cols)
#sort df by index and assign to a new variable
df = df.sort_index()

#what is the average age of athletes in summer games between 1936 and 2000

year_slice = slice(1936, 2000)
season = 'Summer'
df.loc[(year_slice, season), 'Age'].mean()

df.dropna(subset='Medal').loc[(slice(None),slice(None),'Archery'), 'Team'].value_counts()

df.loc[(slice(1980,None),slice(None), slice(None), "Table Tennis Women's Team"), 'Height'].mean()

#tallest tennis player between 1980 and 2016    
df.loc[(slice(1980, 2016), slice(None), 'Tennis', slice(None)), 'Height'].max()

df.loc[idx[1980:2016, :, 'Swimming':'Table tennis'],:]