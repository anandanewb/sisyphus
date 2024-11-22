import time
import timeit
import pandas as pd

cols = ['passenger_count', 'trip_distance', 'total_amount', 'payment_type']
dtypes = {
    'passenger_count': 'int8',
    'trip_distance': 'float32',
    'total_amount': 'float32',
    'payment_type': 'int8'
}   

na_values = {
    'passenger_count': 0,
    'trip_distance': 0,
    'total_amount': 0,
    'payment_type': 0
}

df_list = []
df = pd.read_csv('data/nyc_taxi_2019-01.csv', header=0, usecols=cols )
df_list.append(df)
df = pd.read_csv('data/nyc_taxi_2019-07.csv', header=0, usecols=cols )

df_list.append(df)
dfc = pd.concat(df_list, ignore_index=True)

dfc.passenger_count.value_counts()


timeit.timeit(lambda: dfc.loc[(dfc.payment_type == 2) & (dfc.total_amount >= 1000)], number=3)

#df.loc[(df.payment_type == 2) & (df.total_amount >= 1000)]

timeit.timeit(lambda: dfc.query('payment_type == 2 and total_amount >= 1000'), number = 3)




