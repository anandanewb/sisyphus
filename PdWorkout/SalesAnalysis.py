from matplotlib import pyplot as plt
import pandas as pd
import re
import numpy as np

invoice_no_pattern = r'2425R\d{4}'

# with open('/Users/anand/Downloads/DayBook.csv', 'r') as f:
#     lines = f.readlines()

# with open('/Users/anand/Downloads/DayBook2.csv', 'w') as f:
#     for i, line in enumerate(lines):
#         if i % 2 == 1:
#             line = line.rstrip(',\n')
#             line = re.findall(invoice_no_pattern, line)[0]
#             f.write(line+'\n') 
#         else:
#             line = line.rstrip(',\n')
#             f.write(line.rstrip(',\n')+',')

df = pd.read_csv('~/Downloads/DayBook2.csv', names=['Date', 'Customer_Name', 'Transaction_Type','Amount', 'Invoice_Number']
                 , parse_dates = ['Date']
                 , header=None)

df['Amount'] = abs(df['Amount'])
df['Day_Of_Week'] = df['Date'].dt.day_name()
df['Month'] = df['Date'].dt.month
df['Month_Name'] = df['Date'].dt.month_name()
df['Year'] = df['Date'].dt.year
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
index_levels = ['Year', 'Month', 'Month_Name', 'Day_Of_Week']
df_by_dow = df.groupby(index_levels, sort=False)['Amount'].sum().to_frame()
df_by_dow.index = df_by_dow.index.set_levels(
                                pd.CategoricalIndex(df_by_dow.index.levels[3], 
                                                    categories = days_order, 
                                                    ordered=True), 
                                level="Day_Of_Week")
df_by_dow.sort_index(inplace=True)

# fig, axes = plt.subplots(nrows=5, ncols=1, figsize=(12,4), sharex=True, sharey=True)
# i = 0
# for (year, month, month_name), group in df_by_dow.groupby(['Year', 'Month', 'Month_Name']): 
#     axes[i].plot(group.index.get_level_values('Day_Of_Week'), group.values, label=f'{month_name} {year}')
#     # plt.plot(group.values, group.index.get_level_values('Day_Of_Week'), label=f'{month_name} {year}')
#     axes[i].legend(loc='upper right')
#     i = i+1


fig = plt.figure()

i = 1
for (year, month, month_name), group in df_by_dow.groupby(['Year', 'Month', 'Month_Name']): 
    ax = fig.add_subplot(5,1,i) 
    ax.bar(group.index.get_level_values('Day_Of_Week'), group.values, label=f'{month_name} {year}')
    for j,v in enumerate(group.values):
        ax.text(j, v, f'{v}', ha='center', va='bottom')
    ax.legend(loc='upper right')
    i = i+1



