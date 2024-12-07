import pandas as pd
import numpy as np

cols = ['Year', 'State.Code', 'Total.Math', 'Total.Test-takers', 'Total.Verbal']
index_cols = ['Year', 'State.Code']
df = pd.read_csv('data/sat-scores.csv', usecols=cols, index_col=index_cols)
df.loc[2005, 'Total.Test-takers'].sum()

df.loc[(2010,['NY', 'NJ', 'MA', 'IL']), 'Total.Math'].mean()
df.loc[([2012, 2013, 2014, 2015],['AZ', 'CA', 'TX']), 'Total.Verbal'].mean()
df.loc[(range(2012, 2016), ['AZ', 'CA', 'TX']), 'Total.Verbal'].mean()
df.loc[(slice(None), ['FL', 'IN', 'ID']),['Total.Math', 'Total.Verbal']].mean()
# state that received the highest verbal score and in which year
df.loc[(2013, slice(None)), 'Total.Verbal'].sort_values(ascending=False).head(3)

df.loc[[2005], 'Total.Math'].mean()
df.loc[[2015], 'Total.Math'].mean()

#show average math score in 2005 and 2015 separately    
df.loc[[2005,2015], 'Total.Math'].mean()

df_agg = df.groupby(level=0)['Total.Math'].agg([np.mean, sum])
df_agg.loc[[2005, 2015]]
df.groupby(level=[0,1])['Total.Math'].mean()

