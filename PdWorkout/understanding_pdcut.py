import pandas as pd
import numpy as np

data = list(range(0,11))
bins = [0, 3, 6, 10]

df = pd.DataFrame()

df['data'] = pd.Series(data)

df['include_lowest'] = pd.cut(df['data'], bins=bins, include_lowest=True)
df['exclude_lowest'] = pd.cut(df['data'], bins=bins, include_lowest=False)
print(df)


