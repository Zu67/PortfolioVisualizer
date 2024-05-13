import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Define possible transaction types
transaction_types = ['buy', 'sell']

# Define the number of transactions to generate
num_transactions = 100

# Initialize a list to store the transactions
transactions = []

# Generate the transactions
for _ in range(num_transactions):
    transaction = {
        'date': fake.date(),
        'stock_symbol': fake.lexify(text='????', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        'transaction_type': random.choice(transaction_types),
        'broker': fake.name(),
        'quantity': random.randint(1, 100),
        'price': round(random.uniform(10.0, 500.0), 2)
    }
    transactions.append(transaction)

# Create a DataFrame from the transactions
df = pd.DataFrame(transactions)

# Write the DataFrame to a CSV file
df.to_csv(r'/Users/zubairtahir/Documents/GitHub/PortfolioVisualizer/transactiondata.csv', index=False)