import pandas as pd

tourism_file = 'oecd_tourism.csv'
location_file = 'oecd_locations.csv'
folder = 'data/'
column_names = ['LOCATION', 'SUBJECT', 'TIME', 'Value']

df_tourism = pd.read_csv(folder+tourism_file, usecols=column_names)

df_location = pd.read_csv(folder+location_file, 
                          header=None, 
                          names=['LOCATION', 'NAME'],
                          index_col='LOCATION')

df_tourism.loc[df_tourism['SUBJECT'] == 'INT_REC'].groupby(['LOCATION'])['Value'].mean().sort_values(ascending=False).tail()

df = df_location.join(df_tourism.set_index('LOCATION'))

df.loc[df['SUBJECT'] == 'INT_REC'].groupby(['NAME'])['Value'].mean().sort_values(ascending=False).tail()
