import pandas as pd
import matplotlib.pyplot as plt

cols = ['Plate ID', 'Registration State', 'Vehicle Make', 'Vehicle Color', 'Street Name']
df = pd.read_csv('data/nyc-parking-violations-2020.csv', usecols=cols)

colors = df['Vehicle Color'].dropna()
colors = colors[colors.str.isalpha()]
colors = colors.str.lower()

colors_deduped = colors.drop_duplicates()

