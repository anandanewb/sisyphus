import pandas as pd
import numpy as np

s = pd.read_csv('data/nyc-temps.txt').squeeze()
time_values = np.arange(0,22,3)
num_days = int(len(s)/len(time_values))
hour = np.tile(time_values, num_days)
df = pd.DataFrame({'hour': hour, 'temp': s.values})
df.temp.describe()

df2 = df.copy(deep=True)
df2[df2.hour.isin([3,6])] = np.nan
df2.temp.describe()







