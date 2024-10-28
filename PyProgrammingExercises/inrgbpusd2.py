import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the tickers for INR/USD and GBP/USD
tickers = ["INR=X", "GBP=X"]

# Fetch historical data for the past year
start_date = pd.Timestamp.today() - pd.DateOffset(years=1)
data = yf.download(tickers, start=start_date)

# Extract the latest and earliest exchange rates
inr_usd_latest = data["Adj Close"]["INR=X"][-1]
inr_usd_earliest = data["Adj Close"]["INR=X"][0]
gbp_usd_latest = data["Adj Close"]["GBP=X"][-1]
gbp_usd_earliest = data["Adj Close"]["GBP=X"][0]

# Calculate the percentage increase
inr_usd_increase = ((inr_usd_latest - inr_usd_earliest) / inr_usd_earliest) * 100
gbp_usd_increase = ((gbp_usd_latest - gbp_usd_earliest) / gbp_usd_earliest) * 100

# Calculate INR/GBP
inr_gbp = inr_usd_latest / gbp_usd_latest

# Plot the results with percentage increase
plt.bar(["INR/USD", "INR/GBP"], [inr_usd_latest, inr_gbp])
plt.text(0, inr_usd_latest, f"{inr_usd_increase:.2f}%", ha="center")
plt.text(1, inr_gbp, f"{gbp_usd_increase:.2f}%", ha="center")
plt.xlabel("Exchange Rate")
plt.ylabel("Value")
plt.title("INR/USD vs INR/GBP")
plt.show()