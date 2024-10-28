import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the tickers
tickers = ["INR=X", "GBPINR=X", "AUDINR=X"]

# Get the current date
today = pd.Timestamp.today()
history_years = 10

# Calculate the start date for 5 years ago
start_date = today - pd.DateOffset(years=history_years)

# Fetch the data
data = yf.download(tickers, start=start_date, end=today)

# Extract the relevant columns
inr_usd = data["Adj Close"]["INR=X"]
# gbp_usd = data["Adj Close"]["GBP=X"]
inr_gbp = data["Adj Close"]["GBPINR=X"] 
inr_aud = data["Adj Close"]["AUDINR=X"]

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(inr_usd, label="INR/USD")
plt.plot(inr_gbp, label="INR/GBP")
plt.plot(inr_aud, label="INR/AUD")
plt.title(f"INR vs USD, GBP, AUD Exchange Rates (Last {history_years} Years)")
plt.xlabel("Date")
plt.ylabel("Exchange Rate")
plt.legend()
plt.grid(True)
plt.show()
