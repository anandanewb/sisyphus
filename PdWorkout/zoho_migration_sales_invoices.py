import pandas as pd
import numpy as np


df = pd.read_csv('~/Downloads/invoices_select_legacy.csv')

df['invoice_dt'] = pd.to_datetime(df['Invoice Date'])
df['invoice_year'] = df.invoice_dt.dt.year
df['invoice_month'] = df.invoice_dt.dt.month

# create a column derived from invoice date where value is fiscal year
# starting from 1 April to 31 March
df['fiscal_year'] = np.where(df.invoice_month >= 4, df.invoice_year,  df.invoice_year-1)
df['fiscal_qyear'] = df.invoice_dt.dt.to_period('Q-APR').dt.qyear
df['fiscal_year_prefix'] = ((df.fiscal_year % 100) * 100) + ((df.fiscal_year % 100) + 1)
df['invoice_number_clean'] = np.where(df.fiscal_year.isin([2017,2018])
                                      , df.fiscal_year_prefix.astype(str)+ 'FY' + df["Invoice Number"].astype(str).str.zfill(3)
                                      , df['Invoice Number'])
df.to_csv('~/Downloads/invoices_select_legacy_with_fiscal_year.csv', index=False)

for fisc_year in range(2017,2023):
    df_fisc_year = df[df.fiscal_year == fisc_year]
    df_fisc_year.to_csv(f'~/Downloads/invoices_select_legacy_{fisc_year}.csv', index=False) 

df_errors_FY1718 = pd.read_csv('~/Downloads/invoice_payments_errors_FY1718.csv')
missing_invoices_FY1718 = df_errors_FY1718.invoice_number_clean.drop_dupinvoilicates()

df_missing_invoices_FY1718 = df[df.invoice_number_clean.isin(missing_invoices_FY1718)]
df_missing_invoices_FY1718.to_csv('~/Downloads/invoices_select_legacy_with_fy1718_missing.csv', index=False)

df_errors_FY1819 = pd.read_csv('~/Downloads/invoice_payments_errors_FY1819.csv')
missing_invoices_FY1819 = df_errors_FY1819.invoice_number_clean.drop_duplicates()

df_missing_invoices_FY1819 = df[df.invoice_number_clean.isin(missing_invoices_FY1819)]
df_missing_invoices_FY1819.to_csv('~/Downloads/invoices_select_legacy_with_fy1819_missing.csv', index=False)

df_errors_FY1920 = pd.read_csv('~/Downloads/invoice_payments_errors_FY1920.csv')
missing_invoices_FY1920 = df_errors_FY1920.invoice_number_clean.drop_duplicates()

df_missing_invoices_FY1920 = df[df.invoice_number_clean.isin(missing_invoices_FY1920)]
df_missing_invoices_FY1920.to_csv('~/Downloads/invoices_select_legacy_with_fy1920_missing.csv', index=False)

def get_missing_invoices(fiscal_year, invoice_payment_errors_file):
    df_errors = pd.read_csv(invoice_payment_errors_file)
    missing_invoices = df_errors.invoice_number_clean.drop_duplicates()

    df_missing_invoices = df[df.invoice_number_clean.isin(missing_invoices)]
    return df_missing_invoices

fiscal_year = 2021
payment_errors_file_2021 = '~/Downloads/invoice_payments_errors_FY2021.csv'
df_missing_invoices = get_missing_invoices(fiscal_year, payment_errors_file_2021)
df_missing_invoices.to_csv(f'~/Downloads/invoices_select_legacy_with_fy{fiscal_year}_missing.csv', index=False)



