

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import pandas as pd

# Define the ticker symbol
ticker = "VTI"
benchmark = "SPY"

# Get data for the past 300 days
end_date = datetime.now()
start_date = end_date - timedelta(days=300)

# Get the data for the ticker
data_ticker = yf.download(ticker, start=start_date, end=end_date)

# Get the data for the benchmark
data_benchmark = yf.download(benchmark, start=start_date, end=end_date)

# Print the data
print(f"Data for {ticker}:")
print(data_ticker)
print(f"\nData for {benchmark}:")
print(data_benchmark)

# Define the ticker symbol
ticker = "VTI"
benchmark = "SPY"

# Get data for the past 300 days
end_date = datetime.now()
start_date = end_date - timedelta(days=300)

# Get the data for the ticker
data_ticker = yf.download(ticker, start=start_date, end=end_date)

# Get the data for the benchmark
data_benchmark = yf.download(benchmark, start=start_date, end=end_date)

# Print the data
print(f"Data for {ticker}:")
print(data_ticker)
print(f"\nData for {benchmark}:")
print(data_benchmark)

# Initialize an empty list to store the data
data = []

# Here, df should be a DataFrame that contains information about the constituents of a universe
# For each constituent, create a dictionary of its attributes and append it to the data list
for (universe_symbol, time), constituents in df.items():
    for constituent in constituents:
        row = {
            'UniverseSymbol': universe_symbol,
            'Time': time,
            'Symbol': constituent.Symbol,
            'EndTime': constituent.EndTime,
            'Weight': constituent.Weight,
            'Ticker': constituent.Symbol.Value,
        }
        data.append(row)

# Convert the list of dictionaries into a DataFrame
constituents_df = pd.DataFrame(data)

# Optionally, you can set an index for the DataFrame
constituents_df.set_index(['UniverseSymbol', 'Time', 'Symbol'], inplace=True)

# Define the ticker symbol
ticker = "VTI"
benchmark = "SPY"

# Get data for the past 300 days
end_date = datetime.now()
start_date = end_date - timedelta(days=300)

# Get the data for the ticker
data_ticker = yf.download(ticker, start=start_date, end=end_date)

# Get the data for the benchmark
data_benchmark = yf.download(benchmark, start=start_date, end=end_date)

# Print the data
print(f"Data for {ticker}:")
print(data_ticker)
print(f"\nData for {benchmark}:")
print(data_benchmark)

# Initialize an empty list to store the data
data = []

# Here, df should be a DataFrame that contains information about the constituents of a universe
# For each constituent, create a dictionary of its attributes and append it to the data list
for (universe_symbol, time), constituents in df.items():
    for constituent in constituents:
        row = {
            'UniverseSymbol': universe_symbol,
            'Time': time,
            'Symbol': constituent.Symbol,
            'EndTime': constituent.EndTime,
            'Weight': constituent.Weight,
            'Ticker': constituent.Symbol.Value,
        }
        data.append(row)

# Convert the list of dictionaries into a DataFrame
constituents_df = pd.DataFrame(data)

# Optionally, you can set an index for the DataFrame
constituents_df.set_index(['UniverseSymbol', 'Time', 'Symbol'], inplace=True)

# Reset the index of the DataFrame
constituents_df = constituents_df.reset_index(level='UniverseSymbol', drop=True)

print(constituents_df)

# Define a filter function to select the desired constituents
def filter_function(fundamentals):
    return [fundamental.Symbol for fundamental in fundamentals if fundamental.HasFundamentalData]

# Create a universe using the filter function
universe = filter_function(constituents_df)

# Fetch historical data for the universe constituents
# Specify the period for which you want the historical data
start_date = datetime.now() - timedelta(days=300)
end_date = datetime.now()

# Fetch the historical universe data
df = yf.download(universe, start=start_date, end=end_date)

# Merge the historical universe data with the constituents DataFrame
merged_df = pd.merge(constituents_df, df, left_on=['UniverseSymbol', 'Time', 'Symbol'], right_on=['UniverseSymbol', 'Time', 'Symbol'], how='left')

# Print the merged DataFrame
print(merged_df)

# Initialize an empty list to store the data
data = []

# Iterate through the historical data to collect information
for (universe_symbol, time), constituents in df.items():
    
    for constituent in constituents:
        # For each constituent, create a dictionary of its attributes
        row = {
            'UniverseSymbol': universe_symbol,
            'Time': time,
            'Symbol': constituent.Symbol,
            'EndTime': constituent.EndTime,
            'Price': constituent.AdjustedPrice,
            'Ticker': constituent.Symbol.Value,
            'MarketCap': constituent.MarketCap,
            'Super Sector Code': constituent.AssetClassification.MorningstarEconomySphereCode,
            'Sector Code': constituent.AssetClassification.MorningstarSectorCode,
            'Industry Group Code': constituent.AssetClassification.MorningstarIndustryGroupCode,
            'Industry Code': constituent.AssetClassification.MorningstarIndustryCode,
            'Style': constituent.AssetClassification.StyleScore       
        }
        # Append the dictionary to the data list
        data.append(row)

# Convert the list of dictionaries into a DataFrame
fundamental_df = pd.DataFrame(data)

# Optionally, you can set an index for the DataFrame
fundamental_df.set_index(['UniverseSymbol', 'Time', 'Symbol'], inplace=True)

# Now, `fundamental_df` is a DataFrame with each row representing a constituent
# and its attributes spread across columns.

fundamental_df = fundamental_df.reset_index(level='UniverseSymbol', drop=True)

print(fundamental_df.head())

merged_df = pd.merge(constituents_df, fundamental_df, left_index=True, right_index=True, how='inner')
merged_df = merged_df.reset_index()
print(merged_df.head())

# Creating two separate lookup tables

# Super Sectors lookup table
super_sectors_data = {
    "Super Sector Code": [1, 2, 3],
    "Super Sector": ["Cyclical", "Defensive", "Sensitive"]
}
super_sectors_df = pd.DataFrame(super_sectors_data)

# Sectors lookup table
sectors_data = {
    "Sector Code": [101, 102, 103, 104, 205, 206, 207, 308, 309, 310, 311],
    "Sector": [
        "Basic Materials", "Consumer Cyclical", "Financial Services", "Real Estate",
        "Consumer Defensive", "Healthcare", "Utilities",
        "Communication Services", "Energy", "Industrials", "Technology"
    ]
}
sectors_df = pd.DataFrame(sectors_data)

super_sectors_df, sectors_df


data = [
    {"Industry Group Code": "10110", "Industry Group": "Agriculture", "Industry Code": "10110010", "Industry": "Agricultural Inputs"},
    {"Industry Group Code": "10120", "Industry Group": "Building Materials", "Industry Code": "10120010", "Industry": "Building Materials"},
    {"Industry Group Code": "10130", "Industry Group": "Chemicals", "Industry Code": "10130010", "Industry": "Chemicals"},
    {"Industry Group Code": "10130", "Industry Group": "Chemicals", "Industry Code": "10130020", "Industry": "Specialty Chemicals"},
    {"Industry Group Code": "10140", "Industry Group": "Forest Products", "Industry Code": "10140010", "Industry": "Lumber & Wood Prodcution"},
    {"Industry Group Code": "10140", "Industry Group": "Forest Products", "Industry Code": "10130020", "Industry": "Specialty Chemicals"},
    {"Industry Group Code": "10150", "Industry Group": "Metals & Mining", "Industry Code": "10150010", "Industry": "Aluminum"},
    {"Industry Group Code": "10150", "Industry Group": "Metals & Mining", "Industry Code": "10150020", "Industry": "Copper"},
    {"Industry Group Code": "10150", "Industry Group": "Metals & Mining", "Industry Code": "10150030", "Industry": "Other Industrial Metals & Mining"},
    {"Industry Group Code": "10150", "Industry Group": "Metals & Mining", "Industry Code": "10150040", "Industry": "Gold"},
    {"Industry Group Code": "10150", "Industry Group": "Metals & Mining", "Industry Code": "10150050", "Industry": "Silver"},
    {"Industry Group Code": "10150", "Industry Group": "Metals & Mining", "Industry Code": "10150060", "Industry": "Other Precious Metals & Mining"},
    {"Industry Group Code": "10160", "Industry Group": "Steel", "Industry Code": "10160010", "Industry": "Coking Coal"},
    {"Industry Group Code": "10160", "Industry Group": "Steel", "Industry Code": "10160020", "Industry": "Steel"},
    {"Industry Group Code": "10200", "Industry Group": "Vehicles & Parts", "Industry Code": "10200010", "Industry": "Auto & Truck Dealerships"},
    {"Industry Group Code": "10200", "Industry Group": "Vehicles & Parts", "Industry Code": "10200020", "Industry": "Auto Manufacturers"},
    {"Industry Group Code": "10200", "Industry Group": "Vehicles & Parts", "Industry Code": "10200030", "Industry": "Auto Parts"},
    {"Industry Group Code": "10200", "Industry Group": "Vehicles & Parts", "Industry Code": "10200040", "Industry": "Recreational Vehicles"},
    {"Industry Group Code": "10220", "Industry Group": "Furnishings, Fixtures, & Appliance", "Industry Code": "10220010", "Industry": "Furnishings, Fixtures, & Appliances"},
    {"Industry Group Code": "10230", "Industry Group": "Homebuilding & Construction", "Industry Code": "10230010", "Industry": "Residential Construction"},
    {"Industry Group Code": "10240", "Industry Group": "Manufacturing-Apparel & Accessories", "Industry Code": "10240010", "Industry": "Textile Manufacturing"},
    {"Industry Group Code": "10240", "Industry Group": "Manufacturing-Apparel & Accessories", "Industry Code": "10240020", "Industry": "Apparel Manufacturing"},
    {"Industry Group Code": "10240", "Industry Group": "Manufacturing-Apparel & Accessories", "Industry Code": "10240030", "Industry": "Footwear & Accessories"},
    {"Industry Group Code": "10250", "Industry Group": "Packaging & Containers", "Industry Code": "10250010", "Industry": "Packaging & Containers"},
    {"Industry Group Code": "10260", "Industry Group": "Personal Services", "Industry Code": "10260010", "Industry": "Personal Services"},
    {"Industry Group Code": "10270", "Industry Group": "Restaurants", "Industry Code": "10270010", "Industry": "Restaurants"},
    {"Industry Group Code": "10280", "Industry Group": "Retail—Cyclical", "Industry Code": "10280010", "Industry": "Apparel Retail"},
    {"Industry Group Code": "10280", "Industry Group": "Retail—Cyclical", "Industry Code": "10280020", "Industry": "Department Stores"},
    {"Industry Group Code": "10280", "Industry Group": "Retail—Cyclical", "Industry Code": "10280030", "Industry": "Home Improvement Retail"},
    {"Industry Group Code": "10280", "Industry Group": "Retail—Cyclical", "Industry Code": "10280040", "Industry": "Luxury Goods"},
    {"Industry Group Code": "10280", "Industry Group": "Retail—Cyclical", "Industry Code": "10280050", "Industry": "Internet Retail"},
    {"Industry Group Code": "10280", "Industry Group": "Retail—Cyclical", "Industry Code": "10280060", "Industry": "Specialty Retail"},
    {"Industry Group Code": "10290", "Industry Group": "Travel & Leisure", "Industry Code": "10290010", "Industry": "Gambling"},
    {"Industry Group Code": "10290", "Industry Group": "Travel & Leisure", "Industry Code": "10290020", "Industry": "Leisure"},
    {"Industry Group Code": "10290", "Industry Group": "Travel & Leisure", "Industry Code": "10290030", "Industry": "Lodging"},
    {"Industry Group Code": "10290", "Industry Group": "Travel & Leisure", "Industry Code": "10290040", "Industry": "Resorts & Casinos"},
    {"Industry Group Code": "10290", "Industry Group": "Travel & Leisure", "Industry Code": "10290050", "Industry": "Travel Services"},
    {"Industry Group Code": "10310", "Industry Group": "Asset Management", "Industry Code": "10310010", "Industry": "Asset Management"},
    {"Industry Group Code": "10320", "Industry Group": "Banks", "Industry Code": "10320010", "Industry": "Banks—Diversified"},
    {"Industry Group Code": "10320", "Industry Group": "Banks", "Industry Code": "10320020", "Industry": "Banks—Regional"},
    {"Industry Group Code": "10320", "Industry Group": "Banks", "Industry Code": "10320030", "Industry": "Mortgage Finance"},
    {"Industry Group Code": "10330", "Industry Group": "Capital Markets", "Industry Code": "10330010", "Industry": "Capital Markets"},
    {"Industry Group Code": "10330", "Industry Group": "Capital Markets", "Industry Code": "10330020", "Industry": "Financial Data & Stock Exchanges"},
    {"Industry Group Code": "10340", "Industry Group": "Insurance", "Industry Code": "10340010", "Industry": "Insurance—Life"},
    {"Industry Group Code": "10340", "Industry Group": "Insurance", "Industry Code": "10340020", "Industry": "Insurance—Property & Casualty"},
    {"Industry Group Code": "10340", "Industry Group": "Insurance", "Industry Code": "10340030", "Industry": "Insurance—Reinsurance"},
    {"Industry Group Code": "10340", "Industry Group": "Insurance", "Industry Code": "10340040", "Industry": "Insurance—Specialty"},
    {"Industry Group Code": "10340", "Industry Group": "Insurance", "Industry Code": "10340050", "Industry": "Insurance—Brokers"},
    {"Industry Group Code": "10340", "Industry Group": "Insurance", "Industry Code": "10340060", "Industry": "Insurance—Diversified"},
    {"Industry Group Code": "10350", "Industry Group": "Diversified Financial Services", "Industry Code": "10350010", "Industry": "Shell Companies"},
    {"Industry Group Code": "10350", "Industry Group": "Diversified Financial Services", "Industry Code": "10350020", "Industry": "Financial Conglomerates"},
    {"Industry Group Code": "10360", "Industry Group": "Credit Services", "Industry Code": "10360010", "Industry": "Credit Services"},
    {"Industry Group Code": "10410", "Industry Group": "Real Estate", "Industry Code": "10410010", "Industry": "Real Estate—Development"},
    {"Industry Group Code": "10410", "Industry Group": "Real Estate", "Industry Code": "10410020", "Industry": "Real Estate Services"},
    {"Industry Group Code": "10410", "Industry Group": "Real Estate", "Industry Code": "10410030", "Industry": "Real Estate—Diversified"},
    {"Industry Group Code": "10420", "Industry Group": "REITs", "Industry Code": "10420010", "Industry": "REIT—Healthcare Facilities"},
    {"Industry Group Code": "10420", "Industry Group": "REITs", "Industry Code": "10420020", "Industry": "REIT—Hotel & Motel"},
    {"Industry Group Code": "10420", "Industry Group": "REITs", "Industry Code": "10420030", "Industry": "REIT—Industrial"},
    {"Industry Group Code": "10420", "Industry Group": "REITs", "Industry Code": "10420040", "Industry": "REIT—Office"},
    {"Industry Group Code": "10420", "Industry Group": "REITs", "Industry Code": "10420050", "Industry": "REIT—Residential"},
    {"Industry Group Code": "10420", "Industry Group": "REITs", "Industry Code": "10420060", "Industry": "REIT—Retail"},
    {"Industry Group Code": "10420", "Industry Group": "REITs", "Industry Code": "10420070", "Industry": "REIT—Mortgage"},
    {"Industry Group Code": "10420", "Industry Group": "REITs", "Industry Code": "10420080", "Industry": "REIT—Specialty"},
    {"Industry Group Code": "10420", "Industry Group": "REITs", "Industry Code": "10420090", "Industry": "REIT—Diversified"},
    {"Industry Group Code": "20510", "Industry Group": "Beverages—Alcoholic", "Industry Code": "20510010", "Industry": "Beverages—Brewers"},
    {"Industry Group Code": "20510", "Industry Group": "Beverages—Alcoholic", "Industry Code": "20510020", "Industry": "Beverages—Wineries & Distilleries"},
    {"Industry Group Code": "20520", "Industry Group": "Beverages—Non-Alcoholic", "Industry Code": "20520010", "Industry": "Beverages—Non-Alcoholic"},
    {"Industry Group Code": "20525", "Industry Group": "Consumer Packaged Goods", "Industry Code": "20525010", "Industry": "Confectioners"},
    {"Industry Group Code": "20525", "Industry Group": "Consumer Packaged Goods", "Industry Code": "20525020", "Industry": "Farm Products"},
    {"Industry Group Code": "20525", "Industry Group": "Consumer Packaged Goods", "Industry Code": "20525030", "Industry": "Household & Personal Products"},
    {"Industry Group Code": "20525", "Industry Group": "Consumer Packaged Goods", "Industry Code": "20525040", "Industry": "Packaged Foods"},
    {"Industry Group Code": "20540", "Industry Group": "Education", "Industry Code": "20540010", "Industry": "Education & Training Services"},
    {"Industry Group Code": "20550", "Industry Group": "Retail—Defensive", "Industry Code": "20550010", "Industry": "Discount Stores"},
    {"Industry Group Code": "20550", "Industry Group": "Retail—Defensive", "Industry Code": "20550020", "Industry": "Food Distribution"},
    {"Industry Group Code": "20550", "Industry Group": "Retail—Defensive", "Industry Code": "20550030", "Industry": "Grocery Stores"},
    {"Industry Group Code": "20560", "Industry Group": "Tobacco Products", "Industry Code": "20560010", "Industry": "Tobacco"},{"Industry Group Code": "20610", "Industry Group": "Biotechnology", "Industry Code": "20610010", "Industry": "Biotechnology"},
    {"Industry Group Code": "20620", "Industry Group": "Drug Manufacturers", "Industry Code": "20620010", "Industry": "Drug Manufacturers—General"},
    {"Industry Group Code": "20620", "Industry Group": "Drug Manufacturers", "Industry Code": "20620020", "Industry": "Drug Manufacturers—Specialty & Generic"},
    {"Industry Group Code": "20630", "Industry Group": "Healthcare Plans", "Industry Code": "20630010", "Industry": "Healthcare Plans"},
    {"Industry Group Code": "20645", "Industry Group": "Healthcare Providers & Services", "Industry Code": "20645010", "Industry": "Medical Care Facilities"},
    {"Industry Group Code": "20645", "Industry Group": "Healthcare Providers & Services", "Industry Code": "20645020", "Industry": "Pharmaceutical Retailers"},
    {"Industry Group Code": "20645", "Industry Group": "Healthcare Providers & Services", "Industry Code": "20645030", "Industry": "Health Information Services"},
    {"Industry Group Code": "20650", "Industry Group": "Medical Devices & Instruments", "Industry Code": "20650010", "Industry": "Medical Devices"},
    {"Industry Group Code": "20650", "Industry Group": "Medical Devices & Instruments", "Industry Code": "20650020", "Industry": "Medical Instruments & Supplies"},
    {"Industry Group Code": "20660", "Industry Group": "Medical Diagnostics & Research", "Industry Code": "20660010", "Industry": "Diagnostics & Research"},
    {"Industry Group Code": "20670", "Industry Group": "Medical Distribution", "Industry Code": "20670010", "Industry": "Medical Distribution"},
    {"Industry Group Code": "20710", "Industry Group": "Utilities—Independent Power Producers", "Industry Code": "20710010", "Industry": "Utilities—Independent Power Producers"},
    {"Industry Group Code": "20710", "Industry Group": "Utilities—Independent Power Producers", "Industry Code": "20710020", "Industry": "Utilities—Renewable"},
    {"Industry Group Code": "20720", "Industry Group": "Utilities—Regulated", "Industry Code": "20720010", "Industry": "Utilities—Regulated Water"},
    {"Industry Group Code": "20720", "Industry Group": "Utilities—Regulated", "Industry Code": "20720020", "Industry": "Utilities—Regulated Electric"},
    {"Industry Group Code": "20720", "Industry Group": "Utilities—Regulated", "Industry Code": "20720030", "Industry": "Utilities—Regulated Gas"},
    {"Industry Group Code": "20720", "Industry Group": "Utilities—Regulated", "Industry Code": "20720040", "Industry": "Utilities—Diversified"},
    {"Industry Group Code": "30810", "Industry Group": "Telecommunication Services", "Industry Code": "30810010", "Industry": "Telecom Services"},
    {"Industry Group Code": "30820", "Industry Group": "Media—Diversified", "Industry Code": "30820010", "Industry": "Advertising Agencies"},
    {"Industry Group Code": "30820", "Industry Group": "Media—Diversified", "Industry Code": "30820020", "Industry": "Publishing"},
    {"Industry Group Code": "30820", "Industry Group": "Media—Diversified", "Industry Code": "30820030", "Industry": "Broadcasting"},
    {"Industry Group Code": "30820", "Industry Group": "Media—Diversified", "Industry Code": "30820040", "Industry": "Entertainment"},
    {"Industry Group Code": "30830", "Industry Group": "Interactive Media", "Industry Code": "30830010", "Industry": "Internet Content & Information"},
    {"Industry Group Code": "30830", "Industry Group": "Interactive Media", "Industry Code": "30830020", "Industry": "Electronic Gaming & Multimedia"},
    # Energy Sector
    {"Industry Group Code": "30910", "Industry Group": "Oil & Gas", "Industry Code": "30910010", "Industry": "Oil & Gas Drilling"},
    {"Industry Group Code": "30910", "Industry Group": "Oil & Gas", "Industry Code": "30910020", "Industry": "Oil & Gas E&P"},
    {"Industry Group Code": "30910", "Industry Group": "Oil & Gas", "Industry Code": "30910030", "Industry": "Oil & Gas Integrated"},
    {"Industry Group Code": "30910", "Industry Group": "Oil & Gas", "Industry Code": "30910040", "Industry": "Oil & Gas Midstream"},
    {"Industry Group Code": "30910", "Industry Group": "Oil & Gas", "Industry Code": "30910050", "Industry": "Oil & Gas Refining & Marketing"},
    {"Industry Group Code": "30910", "Industry Group": "Oil & Gas", "Industry Code": "30910060", "Industry": "Oil & Gas Equipment & Services"},
    {"Industry Group Code": "30920", "Industry Group": "Other Energy Sources", "Industry Code": "30920010", "Industry": "Thermal Coal"},
    {"Industry Group Code": "30920", "Industry Group": "Other Energy Sources", "Industry Code": "30920020", "Industry": "Uranium"},
    
    # Industrials Sector
    {"Industry Group Code": "31010", "Industry Group": "Aerospace & Defense", "Industry Code": "31010010", "Industry": "Aerospace & Defense"},
    {"Industry Group Code": "31020", "Industry Group": "Business Services", "Industry Code": "31020010", "Industry": "Specialty Business Services"},
    {"Industry Group Code": "31020", "Industry Group": "Business Services", "Industry Code": "31020020", "Industry": "Consulting Services"},
    {"Industry Group Code": "31020", "Industry Group": "Business Services", "Industry Code": "31020030", "Industry": "Rental & Leasing Services"},
    {"Industry Group Code": "31020", "Industry Group": "Business Services", "Industry Code": "31020040", "Industry": "Security & Protection Services"},
    {"Industry Group Code": "31020", "Industry Group": "Business Services", "Industry Code": "31020050", "Industry": "Staffing & Employment Services"},
    {"Industry Group Code": "31030", "Industry Group": "Conglomerates", "Industry Code": "31030010", "Industry": "Conglomerates"},
    {"Industry Group Code": "31040", "Industry Group": "Construction", "Industry Code": "31040010", "Industry": "Engineering & Construction"},
    {"Industry Group Code": "31040", "Industry Group": "Construction", "Industry Code": "31040020", "Industry": "Infrastructure Operations"},
    {"Industry Group Code": "31040", "Industry Group": "Construction", "Industry Code": "31040030", "Industry": "Building Products & Equipment"},
    {"Industry Group Code": "31050", "Industry Group": "Farm & Heavy Construction Machinery", "Industry Code": "31050010", "Industry": "Farm & Heavy Construction Machinery"},
    {"Industry Group Code": "31060", "Industry Group": "Industrial Distribution", "Industry Code": "31060010", "Industry": "Industrial Distribution"},
    {"Industry Group Code": "31070", "Industry Group": "Industrial Products", "Industry Code": "31070010", "Industry": "Business Equipment & Supplies"},
    {"Industry Group Code": "31070", "Industry Group": "Industrial Products", "Industry Code": "31070020", "Industry": "Specialty Industrial Machinery"},
    {"Industry Group Code": "31070", "Industry Group": "Industrial Products", "Industry Code": "31070030", "Industry": "Metal Fabrication"},
    {"Industry Group Code": "31070", "Industry Group": "Industrial Products", "Industry Code": "31070040", "Industry": "Pollution & Treatment Controls"},
    {"Industry Group Code": "31070", "Industry Group": "Industrial Products", "Industry Code": "31070050", "Industry": "Tools & Accessories"},
    {"Industry Group Code": "31070", "Industry Group": "Industrial Products", "Industry Code": "31070060", "Industry": "Electrical Equipment & Parts"},
        
    # Transportation Sector
    {"Industry Group Code": "31080", "Industry Group": "Transportation", "Industry Code": "31080010", "Industry": "Airports & Air Services"},
    {"Industry Group Code": "31080", "Industry Group": "Transportation", "Industry Code": "31080020", "Industry": "Airlines"},
    {"Industry Group Code": "31080", "Industry Group": "Transportation", "Industry Code": "31080030", "Industry": "Railroads"},
    {"Industry Group Code": "31080", "Industry Group": "Transportation", "Industry Code": "31080040", "Industry": "Marine Shipping"},
    {"Industry Group Code": "31080", "Industry Group": "Transportation", "Industry Code": "31080050", "Industry": "Trucking"},
    {"Industry Group Code": "31080", "Industry Group": "Transportation", "Industry Code": "31080060", "Industry": "Integrated Freight & Logistics"},
    
    # Waste Management Sector
    {"Industry Group Code": "31090", "Industry Group": "Waste Management", "Industry Code": "31090010", "Industry": "Waste Management"},
    
    # Technology Sector
    {"Industry Group Code": "31110", "Industry Group": "Software", "Industry Code": "31110010", "Industry": "Information Technology Services"},
    {"Industry Group Code": "31110", "Industry Group": "Software", "Industry Code": "31110020", "Industry": "Software—Application"},
    {"Industry Group Code": "31110", "Industry Group": "Software", "Industry Code": "31110030", "Industry": "Software—Infrastructure"},
    
    {"Industry Group Code": "31120", "Industry Group": "Hardware", "Industry Code": "31120010", "Industry": "Communication Equipment"},
    {"Industry Group Code": "31120", "Industry Group": "Hardware", "Industry Code": "31120020", "Industry": "Computer Hardware"},
    {"Industry Group Code": "31120", "Industry Group": "Hardware", "Industry Code": "31120030", "Industry": "Consumer Electronics"},
    {"Industry Group Code": "31120", "Industry Group": "Hardware", "Industry Code": "31120040", "Industry": "Electronic Components"},
    {"Industry Group Code": "31120", "Industry Group": "Hardware", "Industry Code": "31120050", "Industry": "Electronics & Computer Distribution"},
    {"Industry Group Code": "31120", "Industry Group": "Hardware", "Industry Code": "31120060", "Industry": "Scientific & Technical Instruments"},
    
    {"Industry Group Code": "31130", "Industry Group": "Semiconductors", "Industry Code": "31130010", "Industry": "Semiconductor Equipment & Materials"},
    {"Industry Group Code": "31130", "Industry Group": "Semiconductors", "Industry Code": "31130020", "Industry": "Semiconductors"},
    {"Industry Group Code": "31130", "Industry Group": "Semiconductors", "Industry Code": "31130030", "Industry": "Solar"}
    ]

# Updating the DataFrame
industry_lookup_df = pd.DataFrame(data)

# Convert 'Industry Group Code' and 'Industry Code' columns to integers
industry_lookup_df['Industry Group Code'] = industry_lookup_df['Industry Group Code'].astype(int)
industry_lookup_df['Industry Code'] = industry_lookup_df['Industry Code'].astype(int)

industry_lookup_df.head()
import matplotlib.pyplot as plt

# Assuming your DataFrame is named final
final = pd.merge(merged_df, super_sectors_df, on='Super Sector Code', how='left')
final = pd.merge(final, sectors_df, on='Sector Code', how='left')
final = pd.merge(final, industry_lookup_df, on=['Industry Group Code', 'Industry Code'], how='left')

print(final.head())

# Step 1: Aggregate the weights by Industry
industry_weights = final.groupby(['Time', 'Sector'])['Weight'].sum()

print(industry_weights.head())

# Step 1: Extract the current index levels
time_index = industry_weights.index.get_level_values('Time')
industry_index = industry_weights.index.get_level_values('Sector')

# Step 2: Convert the 'Time' level to datetime
time_index_datetime = pd.to_datetime(time_index)

# Step 3: Reconstruct the MultiIndex with the updated 'Time' level
new_index = pd.MultiIndex.from_arrays([time_index_datetime, industry_index], names=['Time', 'Sector'])

# Step 4: Set the new MultiIndex to the Series
industry_weights.index = new_index

target_date = pd.to_datetime('2024-03-26')

# Select rows from the Series that have the target date in the 'Time' index level
selected_rows = industry_weights.loc[target_date]

# Step 2: Plotting the pie chart
plt.figure(figsize=(14, 12))
selected_rows.plot.pie(autopct='%1.1f%%', startangle=140)
plt.title('Weight Distribution by Sector for 2023-03-26')
plt.ylabel('')  # Hide the y-label as it's not needed here
plt.show()

# Step 1: Unstack the Series to get a DataFrame
df = industry_weights.unstack(level='Sector')

# Step 2: Plot the DataFrame
plt.figure(figsize=(12, 8))
for column in df.columns:
    plt.plot(df.index, df[column], label=column)

plt.title('Sector Weights Over Time')
plt.xlabel('Date')
plt.ylabel('Weight')
plt.legend(title='Industry', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)  # Rotate dates for better readability
plt.tight_layout()  # Adjust layout to make room for the legend

plt.show()

# Assuming your DataFrame is named final
# Step 1: Aggregate the weights by Super Sector
super_sector_weights = final.groupby(['Time', 'Super Sector'])['Weight'].sum()

# Step 1: Extract the current index levels
time_index = super_sector_weights.index.get_level_values('Time')
super_sector_index = super_sector_weights.index.get_level_values('Super Sector')

# Step 2: Convert the 'Time' level to datetime
time_index_datetime = pd.to_datetime(time_index)

# Step 3: Reconstruct the MultiIndex with the updated 'Time' level
new_index = pd.MultiIndex.from_arrays([time_index_datetime, super_sector_index], names=['Time', 'Super Sector'])

# Step 4: Set the new MultiIndex to the Series
super_sector_weights.index = new_index

target_date = pd.to_datetime('2024-03-26')

# Select rows from the Series that have the target date in the 'Time' index level
selected_rows = super_sector_weights.loc[target_date]

# Step 2: Plotting the pie chart
plt.figure(figsize=(14, 12))
selected_rows.plot.pie(autopct='%1.1f%%', startangle=140)
plt.title('Weight Distribution by Super Sector for 2023-03-26')
plt.ylabel('')  # Hide the y-label as it's not needed here
plt.show()

# Step 1: Unstack the Series to get a DataFrame
df = super_sector_weights.unstack(level='Super Sector')

# Step 2: Plot the DataFrame
plt.figure(figsize=(12, 8))
for column in df.columns:
    plt.plot(df.index, df[column], label=column)

plt.title('Super Sector Weights Over Time')
plt.xlabel('Date')
plt.ylabel('Weight')
plt.legend(title='Industry', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)  # Rotate dates for better readability
plt.tight_layout()  # Adjust layout to make room for the legend

plt.show()

risk_free_rate = 0.05  # Example: 5% annual risk-free rate
risk_free_rate_daily = (1 + risk_free_rate) ** (1/252) - 1

df_security['Return'] = df_security['close'].pct_change()
df_benchmark['Return'] = df_benchmark['close'].pct_change()

df_security['Excess_Return'] = df_security['Return'] - risk_free_rate_daily
market_premium_daily = df_benchmark['Return'] - risk_free_rate_daily

beta = df_security['Return'].cov(df_benchmark['Return']) / df_benchmark['Return'].var()

# Sharpe Ratio daily (without annualizing to see daily variations)
df_security['Sharpe'] = df_security['Excess_Return'] / df_security['Excess_Return'].rolling(window=30).std()

# Treynor Ratio daily (annualizing returns and beta calculation remains constant in this simplification)
df_security['Treynor'] = df_security['Excess_Return'].rolling(window=30).mean() * 252 / beta

# Jensen's Alpha daily
expected_return_daily = risk_free_rate_daily + beta * market_premium_daily
df_security['Jensen_Alpha'] = (df_security['Return'] - expected_return_daily).rolling(window=30).mean() * 252

plt.figure(figsize=(14, 7))
df_security['Sharpe'].plot(label='Sharpe Ratio (30-day rolling)')
df_security['Treynor'].plot(label='Treynor Ratio (30-day rolling)')
df_security['Jensen_Alpha'].plot(label="Jensen's Alpha (30-day rolling)")
plt.title('Rolling Investment Metrics')
plt.xlabel('Date')
plt.ylabel('Metric Value')
plt.legend()
plt.show()

df_security['Cumulative_Returns'] = ((1 + df_security['Return']).cumprod() - 1) * 100
df_benchmark['Cumulative_Returns'] = ((1 + df_benchmark['Return']).cumprod() - 1) * 100

plt.figure(figsize=(14, 7))
df_security['Cumulative_Returns'].plot(label=f'{selected_symbol.Value}')
df_benchmark['Cumulative_Returns'].plot(label=f'{selected_benchmark.Value}')
plt.title('Price Comparison')
plt.xlabel('Date')
plt.ylabel('Price Change (%)')
plt.legend()
plt.show()
