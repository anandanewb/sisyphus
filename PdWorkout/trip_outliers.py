import pandas as pd
import numpy as np

trip_distance = pd.read_csv('data/taxi-distance.csv', header=None).squeeze()


passenger_count = pd.read_csv('data/taxi-passenger-count.csv').squeeze()


df = pd.DataFrame({'trip_distance': trip_distance, 'passenger_count': passenger_count})

iqr = df['trip_distance'].quantile(0.75) - df['trip_distance'].quantile(0.25)
lower_limit = df.trip_distance.quantile(0.25) - 1.5 * iqr
upper_limit = df.trip_distance.quantile(0.75) + 1.5 * iqr
min = int(df.trip_distance.min().round())
max = int(df.trip_distance.max().round())
q1 = int(df.trip_distance.quantile(.25).round())
q3 = int(df.trip_distance.quantile(.75).round())

low_outliers = df[df.trip_distance < lower_limit]
high_outliers = df[df.trip_distance > upper_limit]

high_outliers.describe()


# Short medium and long trips with only one passenger
bins = [min, q1, q3, max] 
pd.cut( df.loc[df.passenger_count == 1].trip_distance, bins=bins, labels=['short', 'medium', 'long']).value_counts()
