import pandas as pd
import glob

data_folder = 'data/'
file_names = ['san+francisco,ca', 
             'new+york,ny',
             'springfield,ma',
             'boston,ma',
             'springfield,il',
             'albany,ny',
             'los+angeles,ca',
             'chicago,il']
extension = '.csv'
cols = [1,2,3]
col_names = [ 'max_temp',
             'min_temp',
             'precipMM']

dfs = []
for file_name in file_names:
    file_path = data_folder + file_name + extension
    df = pd.read_csv(file_path, usecols=cols, names=col_names, skiprows = 1  )
    city, state = file_name.split(',')
    df['city'] = city
    df['state'] = state
    dfs.append(df)

df_all = pd.concat(dfs)

df_all.groupby(['city', 'state']).filter(lambda x: (x.loc[x.precipMM >= 15]).count() >= 3)
