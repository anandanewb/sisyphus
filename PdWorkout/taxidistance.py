import pandas as pd
import numpy as np

s = pd.read_csv('data/taxi-distance.csv',header=None).squeeze()

pd.cut(s, bins=[s.min(), 2, 10, s.max()], include_lowest=True, labels = ['short', 'medium', 'long']).value_counts()
