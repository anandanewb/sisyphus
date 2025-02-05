import pandas as pd
import numpy as np

df = pd.read_csv('~/Downloads/customer_payments_select_legacy.csv')
df = df.dropna(subset=['Invoice Date'])
df['invoice_dt'] = pd.to_datetime(df['Invoice Date'])
df['fiscal_year'] = np.where(df.invoice_dt.dt.month >= 4, df.invoice_dt.dt.year,  df.invoice_dt.dt.year-1)
df['fiscal_year_prefix'] = ((df.fiscal_year % 100) * 100) + ((df.fiscal_year % 100) + 1)
df['invoice_number_clean'] = np.where(df.fiscal_year.isin([2017,2018])
                                      , df.fiscal_year_prefix.astype(str)+ 'FY' + df["Invoice Number"]
                                      , df['Invoice Number'])

df_invoices_missing_payments = pd.read_csv('~/Downloads/Invoices.csv')
df_missing_payments = df.loc[df.invoice_number_clean.isin(df_invoices_missing_payments['Invoice#'].values)]

df_missing_payments.to_csv('~/Downloads/missing_payments.csv')


df.to_csv('~/Downloads/customer_payments_select_legacy_with_fiscal_year.csv', index=False)

for fisc_year  in range(2017,2024):
    df_fisc_year = df[df.fiscal_year == fisc_year]
    df_fisc_year.to_csv(f'~/Downloads/customer_payments_select_legacy_with_FY{fisc_year}.csv', index=False) 