import matplotlib.pyplot as plt
import numpy as np


# x_values = range(0,5)
# y_values = [ x**x for x in range(0,5)]
# plt.plot(x_values, y_values)
# plt.show()
# plt.clf()

# days = [0, 1, 2, 3, 4, 5, 6]

# money_spent = [10, 12, 12, 10, 14, 22, 24]

# money_spent_2 = [11, 14, 15, 15, 22, 21, 12]

# plt.plot(days, money_spent)

# plt.plot(days, money_spent_2)
# plt.show()

# axis and labels
# x = list(range(0,5))
# y = [n**2 for n in x]
# plt.plot(x,y)
# plt.axis([0,3,2,5])
# plt.show()

#labeling the axes
# hours = list(range(9,21))
# happiness = [9.8, 9.9, 9.2, 8.6, 8.3, 9.0, 8.7, 9.1, 7.0, 6.4, 6.9, 7.5]
# plt.plot(hours, happiness)
# plt.xlabel("Time of day")
# plt.ylabel("Happiness Level")
# plt.title("My Happiness Index")
# plt.show()


#subplots
# import matplotlib.pyplot as plt

# x = list(range(1,5))
# y = list(range(1,5))

# plt.subplots_adjust(top=0.5, wspace=0.5, hspace=0.5, bottom=0.2, left=0.5)
# plt.subplot(1,2,1)
# plt.plot(x,y, color='green')
# plt.title('Ist subplot')

# plt.subplot(1,2,2)
# plt.plot(x,y,color='steelblue')
# plt.title('2nd subplot')
# plt.show()

# import matplotlib.pyplot as plt

# plt.subplot(1,2,1)
# plt.plot([-2,-1,0,1,2],[4,1,0,1,4])
# plt.subplot(1,2,2)
# plt.plot([-2,-1,0,1,2], [4,1,0,1,4])
# plt.subplots_adjust(wspace=0.35)

# plt.show()

## Legends

# x = list(range(0,5))
# x_squared = [i**2 for i in x]
# x_cubed = [i**3 for i in x]

# plt.plot(x, x_squared, label='x squared')
# plt.plot(x, x_cubed, label='x cubed')
# plt.legend(loc='center left')

# Modify Ticks
# import matplotlib.pyplot as plt
# ax = plt.subplot(111)
# x = list(range(0,5))
# x_squared = [i**2 for i in x]
# x_cubed = [i**3 for i in x] 
# plt.plot(x, x_squared, label='x squared')
# plt.plot(x, x_cubed, label='x cubed')
# ax.set_xticks([1,2,4])
# ax.set_xticklabels(['one', 'two', 'four'])

#
import matplotlib.pyplot as plt
ax = plt.subplot(3,11)
ax = plt.subplot()
plt.figure(figsize=(4,10))
plt.plot([1, 3, 3.5], [0.1, 0.6, 0.8], 'o', color='k')
ax.set_yticks([0.1, 0.6, 0.8])
ax.set_yticklabels(['10%', '60%', '80%'])
plt.savefig('chart.png')