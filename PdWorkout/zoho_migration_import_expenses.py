import pandas as pd

df1 = pd.read_csv('~/Downloads/expenses_1.csv', parse_dates = ['Expense Date'])
df2 = pd.read_csv('~/Downloads/expenses_2.csv', parse_dates = ['Expense Date'])
df = pd.concat([df1, df2]) 

df['Expense_FiscalYear'] = df['Expense Date'].dt.to_period('Q-MAR').dt.qyear
df['Expense_FiscalQuarter'] = df['Expense Date'].dt.to_period('Q-MAR').dt.quarter

for year in range(2018, 2023):
    for quarter in range(1, 5):
        df_qtr = df[(df['Expense_FiscalYear'] == year) & (df['Expense_FiscalQuarter'] == quarter)]
        df_qtr.to_csv(f'~/Downloads/expenses_{year}Q{quarter}.csv', index=False)