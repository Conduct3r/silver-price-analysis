import pandas as pd 
import matplotlib.pyplot as plt

# loading data
df = pd.read_csv('data/silver_prices.csv')

# converting to datetime
df['Date'] = pd.to_datetime(df['Date'])

print(df.head())

# 7 columns: Date, Open, High, Low, Close, Adj Close, Volume  

# line graph displaying Silver prices over time
plt.figure(figsize = (12,6))

plt.plot(df['Date'], df['Close'])

plt.title("Silver prices over time")

plt.xlabel("Date")

plt.ylabel("Price (USD)")

# plt.show()


print(f"Dataset: SI=F (Silver Futures - COMEX)")

print(f"Source: Yahoo Finance via yfinance")

print(f"Date Range: {df['Date'].min()} to {df['Date'].max()}")

print(f"Total Trading Days: {len(df)}")

# Q1: Which years had the most volatility in silver prices?

df['daily_volatility'] = df['High'] - df['Low']

df['Year'] = df['Date'].dt.year 

volatility_by_year = df.groupby('Year')['daily_volatility'].mean()

print(volatility_by_year)

# 2025, followed by 2024 and 2020 ( Potentially COVID related )

# Volatility of January 2026 compared to previous Januarys
df['Month'] = df['Date'].dt.month

january_volatility = df[df['Month'] == 1].groupby('Year')['daily_volatility'].mean()

print("January volatility by year:")

print(january_volatility)

# the volatility present in January 2026 ( $3.96 ) is the biggest in the last 10 years for Silver
