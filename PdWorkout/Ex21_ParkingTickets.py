import pandas as pd
import numpy as np

date_cols = ['Issue Date']

nondate_cols = ['Date First Observed', 'Plate ID', 'Registration State', 'Vehicle Make'
        , 'Street Name', 'Vehicle Color']

all_cols = date_cols + nondate_cols

df = pd.read_csv('data/nyc-parking-violations-2020.csv', usecols=all_cols, parse_dates = date_cols )
df.set_index('Issue Date', inplace=True)
df.loc['2020-01-02', 'Vehicle Make'].value_counts().head(3)
df.loc['2020-06-01', 'Street Name'].value_counts().head(5)

df.reset_index(inplace=True).set_index(['Vehicle Color'], inplace=True)
df.loc[['Red', 'Blue'], ['Vehicle Make']].value_counts().head(5)