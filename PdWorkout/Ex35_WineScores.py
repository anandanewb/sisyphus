# Ex35_Wine_scores

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


column_names = ['country_code', 'country_name']
oecd_df = pd.read_csv('data/oecd_locations.csv', names=column_names, header=None, index_col = 'country_code')


tourism_col_names = ['LOCATION', 'TIME', 'SUBJECT', 'Value']
oecd_tourism_df = pd.read_csv('data/oecd_tourism.csv', usecols=tourism_col_names
                              ,  index_col = ['LOCATION'])
                            


tourism_spending = oecd_df.join(oecd_tourism_df, how='inner').groupby('country_name')['Value'].mean()

wine_cols = ['country', 'points']
wine_df = pd.read_csv('data/winemag-150k-reviews.csv', usecols=wine_cols) 
country_points = wine_df.groupby('country').mean().sort_values(by='points', ascending=False)

country_points.join(tourism_spending, how='right')
country_points.join(tourism_spending, how='outer').corr()




