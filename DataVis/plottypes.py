#plottypes
import matplotlib.pyplot as plt
import pandas as pd

heights = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
x_values = range(len(heights))
plt.bar(x_values, heights)


#simple bar chart
days_in_year = list(heights)
plt.bar(range(len(days_in_year)), days_in_year)
plt.show()

#simple bar chart I
ax = plt.subplot()
ax.set_xticks(range(0,9))
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
ax.set_xticklabels(planets, rotation=75)
ax.bar(range(len(days_in_year)), days_in_year)
plt.xlabel('Planets')
plt.ylabel('Days in a year')

#side by side bars

## China Data (Blue Bars)
n = 1  # 1/2 Dataset
t = 2  # Number of datasets
d = 7  # Number of sets of bars
w = 0.8 # Width of each bar
x_values1 = [t*element + w*n for element in range(d)]

# US data (Orange Bars)
n = 2  # 2/2 Dataset
t = 2  # Number of datasets
d = 7  # Number of sets of bars
w = 0.8 # Width of each bar
x_values2 = [t*element + w*n for element in range(d)]

plotdata = pd.DataFrame({
    "ChinaData": x_values1,
    "USData": x_values2
}, index=range(len(x_values1)))

plotdata.plot(kind="bar")
