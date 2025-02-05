import pandas as pd

cols = ['passenger_count', 'trip_distance', 'total_amount']

df = pd.read_csv('data/nyc_taxi_2019-01.csv',
                 usecols = cols,
                 dtype = {'passenger_count': 'Int64',
                          'trip_distance': 'float64',
                          'total_amount': 'float64'}
                         )



df.groupby(['passenger_count'])['total_amount'].mean().sort_values()
df.groupby(['passenger_count'])['total_amount'].mean().sort_index()
df.groupby(['passenger_count'])['total_amount'].agg(['mean', 'min', 'median', 'max', 'count'])