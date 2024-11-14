import numpy as np
import pandas as pd
import calendar


g = np.random.default_rng(0)

s = pd.Series( g.normal(20,5,28), index= list(calendar.day_abbr) * 4).round().astype(np.int8)
print(s)




