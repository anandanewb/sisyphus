import pandas as pd


col_newnames = ['Year', 'State.Code', 'Total.Math', 
             '20k<40k.Math', 
             '40k<60k.Math',
             '60k<80k.Math', 
             '80k<100k.Math','0K<20k.Math',
             '100k<.Math']

col_names = ['Year', 'State.Code', 'Total.Math', 
            'Family Income.Between 20-40k.Math',
            'Family Income.Between 40-60k.Math',
            'Family Income.Between 60-80k.Math',
            'Family Income.Between 80-100k.Math',
            'Family Income.Less than 20k.Math',
            'Family Income.More than 100k.Math']
            

df = pd.read_csv('data/sat-scores.csv', usecols=col_names)
df.columns = col_newnames


# Find average SAT math score for each income level, grouped and then sorted by year
df.groupby(['Year']).mean(numeric_only=True).sort_index()
df.groupby(['Year', 'State.Code']).mean(numeric_only=True).sort_index()

df.groupby(['Year']).mean(numeric_only=True).T.pct_change().round(4)*100




# beyond the exercise

# filtering and transforming

import numpy as np
import pandas as pd
np.random.seed(0)

df = pd.DataFrame( {
    'name': list('ABCDEFGHIJ'),
    'year': [2018, 2019, 2020] * 3 + [2021],
    'score': np.random.randint(80, 100, 10)
})

df.loc[df.score > 90]
df.groupby('year').filter(lambda df: df.score.mean() > 90)
df['mean'] = df.groupby('year').score.transform(np.mean)
df['mean_diff'] = df.groupby('year').score.transform(lambda x: x - x.mean())