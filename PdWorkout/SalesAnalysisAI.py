import pandas as pd
import matplotlib.pyplot as plt

# Your data (from the first input)
data = {'Year': [2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2024, 2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025, 2025],
        'Month': [10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
        'Month_Name': ['October', 'October', 'October', 'October', 'October', 'October', 'October', 'November', 'November', 'November', 'November', 'November', 'November', 'November', 'December', 'December', 'December', 'December', 'December', 'December', 'December', 'January', 'January', 'January', 'January', 'January', 'January', 'January', 'February', 'February', 'February', 'February', 'February', 'February', 'February'],
        'Day_Of_Week': ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday', 'Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday', 'Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday', 'Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday', 'Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday'],
        'Value': [443852.04, 393140.0, 245420.0, 167200.0, 194700.0, 438300.0, 197810.0, 467811.0, 110540.0, 489660.0, 240350.0, 193400.0, 279520.0, 299180.0, 125940.0, 361380.0, 319300.0, 410660.0, 195160.0, 76550.0, 297330.0, 317070.0, 267703.0, 55645.0, 91208.0, 199338.0, 173499.0, 224410.0, 114800.0, 240075.0, 92160.0, 38000.0, 111900.0, 85415.0, 207940.0]}

df = pd.DataFrame(data)

# ... (rest of the code is exactly the same as the corrected version I provided earlier)
# ... (including the categorical conversion, the loop, the merge, and the plotting)
# ... (no changes needed)

# Convert 'Day_Of_Week' to categorical and specify order
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['Day_Of_Week'] = pd.Categorical(df['Day_Of_Week'], categories=days_order, ordered=True)

# Create subplots for each month
fig, axes = plt.subplots(2, 3, figsize=(15, 8))  # Adjust rows and columns as needed
months = df['Month_Name'].unique()
axes = axes.flatten()  # Flatten the axes array for easier iteration

for i, month in enumerate(months):
    month_data = df[df['Month_Name'] == month]

    # Create a DataFrame with ALL days of the week and NaN for missing values
    all_days = pd.DataFrame({'Day_Of_Week': days_order})  # DataFrame with all days
    merged_data = pd.merge(all_days, month_data, on='Day_Of_Week', how='left')  # Merge, keep all days

    axes[i].bar(merged_data['Day_Of_Week'], merged_data['Value'])  # Use merged data
    axes[i].set_title(month)
    axes[i].set_xlabel("Day of Week")
    axes[i].set_ylabel("Sales Amount")
    axes[i].tick_params(axis='x', rotation=45) # Rotate x-axis labels if needed

# Adjust layout to prevent overlapping titles/labels
plt.tight_layout()
plt.show()