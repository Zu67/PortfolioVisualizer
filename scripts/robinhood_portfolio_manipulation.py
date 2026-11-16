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

# Convert 'Activity Date' to datetime
df['Activity Date'] = pd.to_datetime(df['Activity Date'])

df.dropna(inplace=True)

# Create a new dataframe with all dates for each symbol
all_dates = pd.date_range(start=df['Activity Date'].min(), end=df['Activity Date'].max())
all_symbols = df['Instrument'].unique()
new_df = pd.DataFrame([(date, symbol) for date in all_dates for symbol in all_symbols], columns=['Activity Date', 'Instrument'])

# Merge the new dataframe with the original dataframe
df = pd.merge(new_df, df, on=['Activity Date', 'Instrument'], how='left')

# Calculate the holding cost
df['Holding Cost'] = df['Amount'] * -1

# Adjust 'Quantity' based on the sign of 'Holding Cost'
df['Quantity'] = df.apply(lambda row: -row['Quantity'] if row['Holding Cost'] < 0 else row['Quantity'], axis=1)


# Calculate the aggregated quantity and average price
df['Aggregated Quantity'] = df.groupby('Instrument')['Quantity'].cumsum()
df['Aggregated Quantity'] = round(df['Aggregated Quantity'], 2)
df['Total Cost'] = df.groupby('Instrument')['Holding Cost'].cumsum()
df['Average Price'] = df['Total Cost'] / df['Aggregated Quantity']
df['Average Price'] = round(df['Average Price'], 2)

# Fill forward the values
df[['Quantity', 'Aggregated Quantity', 'Average Price']] = df.groupby('Instrument')[['Quantity', 'Aggregated Quantity', 'Average Price']].fillna(method='ffill')

df = df[['Activity Date', 'Instrument', 'Aggregated Quantity', 'Average Price']]

#Get Price Data

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

df['Total Cost'] = df['Aggregated Quantity'] * df['Average Price']

df['Gain/Loss'] = df['Market Value'] - df['Total Cost']

df = df[['Activity Date', 'Instrument', 'Aggregated Quantity', 'Average Price', 'adjusted_close', 'Market Value', 'Gain/Loss']]


print(df.tail(25))