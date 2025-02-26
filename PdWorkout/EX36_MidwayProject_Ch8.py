# EX36_MidwayProject_Ch8

import pandas as pd
import numpy as np

file_name = 'data/2020_sharing_data_outside.csv'
general_columns = ['age', 'are.you.datascientist', 'is.python.main' , 'company.size'
                   , 'country.live', 'employment.status' , 'first.learn.about.main.ide', 'how.often.use.main.ide'
                    , 'main.purposes', 'missing.features.main.ide', 'nps.main.ide', 'python.version.most'
                    , 'python.years', 'python2.version.most', 'python3.version.most', 'several.projects'
                    , 'team.size', 'use.python.most', 'years.of.coding' ]

def get_column_multi_name(column_name):
    try: 
        if column_name in general_columns:
            return ('general', column_name)
        else:
            first, last_rest = column_name.rsplit('.', 1)
            return (first, last_rest)
    except ValueError as e:
        print(f'{column_name} generated {e}') 

df = pd.read_csv(file_name)

df.columns = (pd.MultiIndex.from_tuples(
                [get_column_multi_name(one_column_name) for one_column_name in df.columns]))


df = df.sort_index(axis=1)
df[('ide', 'main')].value_counts(ascending=True)
df['other.lang'].count().sort_values(ascending=False)


#create a random dataframe to understand count(axis=1)

# num_rows = 3
# num_columns = 5

# random_data = np.random.rand(num_rows, num_columns)
# nan_mask = np.random.rand(num_rows, num_columns) < 0.2
# random_data[nan_mask] = np.nan

# random_df = pd.DataFrame(random_data)

df[('general', 'country.live')].value_counts(normalize=True).head(10).round(decimals=4)*100

vc_n = df[('general','python.years')].value_counts(normalize=True)
vc = df[('general', 'python.years')].value_counts()

new_df = pd.DataFrame({'count': vc, 'percentage': vc_n})

df['general'].loc[df[('general', 'python.years')] == '11+ years']['country.live'].value
