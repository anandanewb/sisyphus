import pandas as pd

use_cols = ['passenger_count', 'total_amount', 'payment_type']
df19 = pd.read_csv('data/nyc_taxi_2019-07.csv',  usecols =use_cols)
df19['year'] = 2019
df20 = pd.read_csv('data/nyc_taxi_2020-07.csv',  usecols =use_cols)
df20['year'] = 2020

dfc = pd.concat([df19, df20], ignore_index=True)    

dfc.loc[dfc.year == 2019, 'total_amount'].sum().round(2)
dfc.loc[dfc.year == 2020, 'total_amount'].sum().round(2)

dfc.groupby('year').total_amount.sum().round(2) 


# were people more likely to use cash during the pandemic? How to 
# show percentages of the total amount of money collected by payment type?
dfp = dfc.groupby(['year', 'payment_type']).size().unstack()

row_sums = dfp.sum(axis=1)

df_normalized = dfp.div(row_sums, axis=0).mul(100).round(2).astype('str') + '%'
dfc.loc[dfc.year==2019][['passenger_count']].value_counts(normalize=True).mul(100).round(2).astype('str') + '%'
dfc.loc[dfc.year==2020][['passenger_count']].value_counts(normalize=True).mul(100).round(2).astype('str') + '%'
dfc[dfc.year==2019].groupby(['passenger_count'])[['passenger_count']].value_counts(normalize=True).mul(100).round(2).astype('str') + '%'