import pandas as pd
import numpy as np

df = pd.read_json('data/cities.json')
df.sort_values(by='population', ascending=False).describe().round().loc[['mean', '50%']]

df.growth_from_2000_to_2013.replace('', '0%', inplace=True)
df['growth_fp'] = df.growth_from_2000_to_2013.str[:-1].astype(float)/100
df.growth_fp.describe().loc[['mean', '50%']]
bins=[-np.inf, 0, np.inf]
labels = ['-ve', '+ve'] 

df['Growth_category'] = pd.cut(df.growth_fp, bins=bins, labels = labels)
df.Growth_category.value_counts()


df[abs(df.latitude) > df.latitude.mean() + (2 * df.latitude.std())]
df.latitude.mean()
df.latitude.std()

df.loc[df.latitude == df.latitude.max(), ['city', 'state', 'rank']]
df['state'].value_counts().head(5)
df['state'].value_counts().tail(5)


