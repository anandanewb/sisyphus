import numpy as np
import pandas as pd

s = pd.read_csv('data/taxi-passenger-count.csv', header=None).squeeze()
print(s.head(5))

# min = s.loc[s==1].count() / s.count() * 100
# max = s.loc[s==6].count() / s.count() * 100


sv = s.value_counts(normalize=True)[[1,6]]

print(f'Min(%): {sv[1] * 100}, Max(%): {sv[6] * 100}')


