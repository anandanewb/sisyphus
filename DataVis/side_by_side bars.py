# side_by_side bars
#https://www.geeksforgeeks.org/plotting-multiple-bar-charts-using-matplotlib-in-python/
import numpy as np
import matplotlib.pyplot as plt

X = ['Group A','Group B','Group C','Group D']
Ygirls = [10, 20, 20, 40]
Zboys = [20, 30, 25, 30]
others = [15, 20, 25, 30]

X_axis = np.arange(1,len(X)+1)
width = 0.5
plt.bar(X_axis - width, Ygirls, width, label = 'Girls')
plt.bar(X_axis, others, width, label = 'Others')
plt.bar(X_axis + width, Zboys, width, label = 'Boys')

plt.xticks(X_axis)
plt.xlabel("Groups")
plt.ylabel("Number of Students")
plt.title("Number of Students in each group")
plt.legend()
plt.tight_layout
plt.show()