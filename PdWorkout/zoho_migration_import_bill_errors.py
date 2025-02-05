import numpy as np
import pandas as pd

fiscal_year = 2122
fiscal_quarter = 4
file_name = f'~/Downloads/errors_{fiscal_year}Q{fiscal_quarter}.csv'
new_file_name = f'~/Downloads/errors_{fiscal_year}Q{fiscal_quarter}_new.csv'
df = pd.read_csv(file_name)

# In the string "The given total value 20,521 and the system generated total value 20,520.99 are not same."
# extract the two values and get their difference
def get_difference(errorMessage):
    given_value = errorMessage.extract(r'The given total value ([\d{1,},]+(?:\.\d{2})?)')
    system_value = errorMessage.extract(r'the system generated total value ([\d{1, }, ]+(?:\.\d{2})?)')
    return given_value - system_value


df['new_rate'] = np.where(df['Item Details Type'] == 'AccountBasedExpenseLineDetail', 
                          (df['Rate'] + \
                          (df['ERRORMESSAGE'].str.extract(r'The given total value ([\d,.]+)')[0].str.replace(',', '').astype(float) - \
                          df['ERRORMESSAGE'].str.extract(r'the system generated total value ([\d,.]+)')[0].str.replace(',', '').astype(float))).round(decimals=2), 
                          df['Rate'])

# Roundoff values are the same for both rate and total since quantity is always 1
df['new_ItemTotal'] = np.where(df['Item Details Type'] == 'AccountBasedExpenseLineDetail',
                               df['new_rate'],
                               df['Item Total'])
df.to_csv(new_file_name, index=False)