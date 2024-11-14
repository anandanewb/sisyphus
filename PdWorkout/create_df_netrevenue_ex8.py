import pandas as pd
import numpy as np

ids = [23, 96, 97, 15, 87]
names = ['computer', 'python workout', 'pandas workout', 'banana', 'sandwich'] 
wholesale_price = [500, 35, 35, 0.5, 3.0] 
retail_price = [1000, 75, 75, 1, 5]
sales = [100, 1000, 500, 200, 300]
df = pd.DataFrame( { 'id': ids,
                'product_name': names,
                'wholesale_price': wholesale_price,
                'retail_price': retail_price, 'monthly_sales': sales  }) 
total_sales = ((df.retail_price - df.wholesale_price) * df.monthly_sales).sum()

df['net_income'] = (df.retail_price - df.wholesale_price) * df.monthly_sales
df['net_income_15'] = df.net_income * 0.85
df["net_income_20"] = df.net_income * 0.80
df["net_income_25"] = df.net_income * 0.75
df.sum()

# 25% on products more than 20000

df['discounted_net'] = np.where(df['net_income'] > 20000, df['net_income'] * 0.75, df['net_income'])    
df.discounted_net.sum()

bins = [0, 30, 80, 1001 ]

labels = ['0%', '10%', '25%'] 
df['progressive_tax'] = pd.cut(df.retail_price, bins=bins, labels=labels)
numeric_cols = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col])]
df_formatted = df.style.format({col: '{:,.2f}' for col in numeric_cols})
