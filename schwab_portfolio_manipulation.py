import pandas as pd
import yfinance as yf

# Load the CSV file into a DataFrame
df = pd.read_csv(r'Roth_IRA.csv')

# Convert the 'Date' column to datetime and handle errors
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
# Drop rows with NaT in the 'Date' column
df = df.dropna(subset=['Date'])

# Create a new dataframe with all dates for each symbol
all_dates = pd.date_range(start=df['Date'].min(), end=df['Date'].max())
all_symbols = df['Symbol'].unique()
new_df = pd.DataFrame([(date, symbol) for date in all_dates for symbol in all_symbols], columns=['Date', 'Symbol'])

# Sort by 'Date' from low to high
df = df.sort_values(by='Date')
df = df[df['Action'].isin(['Buy', 'Sell'])]

# Remove dollar signs and commas, and convert to float
df['Quantity'] = df['Quantity'].apply(lambda x: str(x).replace(',', '').replace('$', '')).astype(float)
df['Price'] = df['Price'].apply(lambda x: str(x).replace(',', '').replace('$', '')).astype(float)
df['Amount'] = df['Amount'].apply(lambda x: str(x).replace(',', '').replace('$', '')).astype(float)

#print(df.tail())

# Merge the new dataframe with the original dataframe
df = pd.merge(new_df, df, on=['Date', 'Symbol'], how='left')

# Print the DataFrame
#print(df.head(10))

df['Holding Cost'] = df['Amount'] * -1

df['Quantity'] = df.apply(lambda row: -row['Quantity'] if row['Holding Cost'] < 0 else row['Quantity'], axis=1)

# Calculate the aggregated quantity and average price
df['Aggregated Quantity'] = df.groupby('Symbol')['Quantity'].cumsum()
df['Aggregated Quantity'] = round(df['Aggregated Quantity'], 2)
df['Total Cost'] = df.groupby('Symbol')['Holding Cost'].cumsum()
df['Average Price'] = df['Total Cost'] / df['Aggregated Quantity']
df['Average Price'] = round(df['Average Price'], 2)

# Fill forward the 'Symbol', 'Aggregated Quantity', and 'Average Price' columns
df[['Quantity', 'Aggregated Quantity', 'Average Price']] = df.groupby('Symbol')[['Quantity', 'Aggregated Quantity', 'Average Price']].fillna(method='ffill')

print(df.tail())
