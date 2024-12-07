import pandas as pd
import numpy as np

#read the data/energy_1.csv file

names = ['consumption_kwh', 'cost_£', 'start', 'end']
dates = ['start', 'end']
dtype = {'consumption_kwh': np.float64, 'cost_£': np.float64}

def parse_custom_date(date_str):
    # Custom parsing function if needed
    return pd.to_datetime(date_str, format='%Y-%m-%dT%H:%M:%S%z')

dfs = []
dfs.append(pd.read_csv('data/energy_1.csv', header=None
          ,skiprows=1
          ,names = names
          ,parse_dates = dates
          ,dtype = dtype)
          )

dfs.append(pd.read_csv('data/energy_2.csv', header=None
          ,skiprows=1   
          ,names = names
          ,parse_dates = dates
          ,dtype = dtype))

df = pd.concat(dfs, ignore_index=True)

df['start'] = pd.to_datetime(df['start'], utc=True)
df['end'] = pd.to_datetime(df['end'], utc=True)
