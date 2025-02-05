import pandas as pd

cols = ['Plate ID', 'Registration State', 'Vehicle Make'
        , 'Vehicle Color','Violation Time', 'Street Name']


df = pd.read_csv('data/nyc-parking-violations-2020.csv', usecols=cols)

missed_fees = (len(df) - len(df.dropna())) * 100
subset_cols = ['Plate ID', 'Registration State', 'Vehicle Make', 'Street Name']
df2 = df.dropna(subset=subset_cols)
missed_fees2 = (len(df) - len(df2)) * 100

df3 = df.dropna(subset=subset_cols, thresh=3)
missed_fees3 = (len(df) - len(df3)) * 100

df4 = df[df['Plate ID'] == 'BLANKPLATE']

dfcopy = df.__deepcopy__()
dfcopy.replace('BLANKPLATE', pd.NA, inplace=True)