import pandas as pd
import yfinance as yf
import math

# Read the CSV file
df = pd.read_csv('robinhood_data.csv', on_bad_lines='skip')

# Remove dollar sign, parentheses and convert 'Price' and 'Amount' to float
df['Price'] = pd.to_numeric(df['Price'].replace('[\$,]', '', regex=True).replace('\((.*)\)', '-\\1', regex=True), errors='coerce')
df['Amount'] = pd.to_numeric(df['Amount'].replace('[\$,]', '', regex=True).replace('\((.*)\)', '-\\1', regex=True), errors='coerce')

# Convert 'Quantity' to float
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

# Convert the 'Activity Date' column to datetime
df['Activity Date'] = pd.to_datetime(df['Activity Date'])

# Calculate the holding cost
df['Holding Cost'] = df['Amount'] * -1

# Adjust 'Quantity' based on the sign of 'Holding Cost'
df['Quantity'] = df.apply(lambda row: -row['Quantity'] if row['Holding Cost'] < 0 else row['Quantity'], axis=1)

# Sort by 'Instrument' and 'Activity Date'
df.sort_values(by=['Activity Date'], inplace=True)

df = df.dropna()

# Calculate the aggregated quantity and average price
df['Aggregated Quantity'] = df.groupby('Instrument')['Quantity'].cumsum()
df['Aggregated Quantity'] = round(df['Aggregated Quantity'], 2)
df['Total Cost'] = df.groupby('Instrument')['Holding Cost'].cumsum()
df['Average Price'] = df['Total Cost'] / df['Aggregated Quantity']
df['Average Price'] = round(df['Average Price'], 2)

# Get the unique tickers
tickers = list(df['Instrument'].unique())
# Remove 'nan' from the list
tickers = [x for x in tickers if x == x]

# Get the start and end dates
start_date = df['Activity Date'].min().strftime('%Y-%m-%d')
end_date = df['Activity Date'].max().strftime('%Y-%m-%d')

# Download the historical data
data = yf.download(tickers, start=start_date, end=end_date)

data = data['Adj Close'].stack().reset_index()

data = data.rename(columns={0: 'adjusted_close'})

# Merge the dataframes
df = df.merge(data, left_on=['Instrument', 'Activity Date'], right_on=['Ticker', 'Date'])

df['Market Value'] = df['Aggregated Quantity'] * df['adjusted_close']

df['Gain/Loss'] = df['Market Value'] - df['Total Cost']

df = df[['Activity Date', 'Instrument', 'Quantity', 'Aggregated Quantity', 'Average Price', 'adjusted_close', 'Market Value', 'Gain/Loss']]

# Print the result
print(df[df['Instrument'] == 'ITOT'])