import pandas as pd

filename = 'data/olympic_athlete_events.csv'
cols = ['Age', 'Height', 'Team', 'Year', 'Season', 'Sport', 'Medal']
year_slice = slice(1980,None) 
countries = ['Britain', 'France', 'United States', 'Switzerland', 'China', 'India']

df = pd.read_csv(filename, usecols=cols)
df2 = df.loc[df['Team'].isin(countries)]
df3 = df2.loc[df.Year >= 1980]
df4 = df.loc[df.Team.isin(countries) & (df.Year >= 1980)]

df = df3
df.pivot_table(index='Year', columns='Team', values='Age', aggfunc='mean'   )

df.pivot_table(index='Sport', columns='Year', values='Height', aggfunc=['max','mean'])

pd.pivot_table(df.dropna(subset='Medal'),
               index='Year',
               columns='Team',
               values='Medal',
               aggfunc='size',
               fill_value=0)


pd.pivot_table(df.dropna(subset='Medal'),
               index='Year',
               columns='Team',
               values='Medal',
               aggfunc='count',
               fill_value=0)

pd.pivot_table(df.dropna(subset='Medal'),
               index=['Year', 'Season'],
               columns='Team',
               values='Medal',
               aggfunc='count',
               fill_value=0)

pd.pivot_table(df.dropna(subset='Medal'),
               index='Year',
               columns='Team',
               values=['Age', 'Height'],
               aggfunc='mean',
               fill_value=0,
               margins=True)

pd.swaplevel(0,1,axis=1).sort_index(axis=1)