# PortfolioVisualizer

Python scripts for positions built from a brokerage export and for prices from Yahoo Finance. The exports themselves are not in this repository.

| Script | What it does |
| --- | --- |
| `scripts/Data Generator.py` | Uses Faker to write 100 rows to a local `transactiondata.csv`. Each row is a date, a four-letter symbol, buy or sell, a fake person's name in the broker column, a quantity from 1 to 100, and a price from 10.00 to 500.00. |
| `scripts/portfolio_calculation_quinn.py` | Reads `robinhood_data.csv`. A dollar sign or comma is removed, and an amount in parentheses is read as negative. Holding cost is that amount times -1, so a positive amount becomes a negative cost and flips the quantity's sign. Average price is the running cost divided by the running quantity. Rows with a missing field are dropped. It does not expand the calendar. It inner-joins adjusted closes on the activity date, so a trade with no close that day is dropped, and it prints only the ITOT rows. |
| `scripts/robinhood_portfolio_manipulation.py` | Reads the same file. A dollar sign or comma is removed, and an amount in parentheses is read as negative, before any row with a missing field is dropped. It does not keep only buys and sells. Holding cost is the amount times -1, and quantity flips sign when that cost is negative. It expands every calendar day from the first remaining date through the last, for every remaining symbol, then forward-fills aggregated quantity and average price. The price join is an inner join, so a day with no adjusted close is dropped. Total cost becomes aggregated quantity times average price. It prints the last 25 rows. |
| `scripts/schwab_portfolio_manipulation.py` | Reads `Roth_IRA.csv`. The calendar and the symbol list are built from every row that has a date, including rows that are not a buy or a sell. It then keeps only Buy and Sell, applies the same holding-cost sign flip, and forward-fills quantity, aggregated quantity, and average price. It imports `yfinance` and does not call it. It prints the last 5 rows. |
| `scripts/PortfolioVisualizerInGit.py` | Prints two downloads of about 300 days of VTI and SPY, then stops. See below. |
| `scripts/PortfolioData` | Reads a local `PortfolioData.csv` and plots the running sum of daily percent changes. The chart title is "Portfolio Performance". |
| `scripts/plaid_quickstart.py` | Notes for running the public Plaid quickstart. It does not contain API keys. |

`scripts/PortfolioVisualizerInGit.py` prints two downloads of about 300 days of VTI and SPY. The next loop reads `df`, which this file has not assigned, so running it from the top stops there. The lines after that are not reached. They expect `df` to be a constituents table, build Morningstar-style super-sector, sector, and industry lookup tables, and plot sector and super-sector weights. Those pie charts select `2024-03-26` and the titles say `2023-03-26`. The last cells use `df_security`, `df_benchmark`, `selected_symbol`, and `selected_benchmark`, which are also not defined here. They compute a beta, a 30-day rolling Sharpe ratio, Treynor ratio, and Jensen's alpha with a 5% risk-free rate, and plot cumulative percent price change.

`data/ETF Constituent Data - Examples.csv` is example ETF constituent data.

`quickstart` is a gitlink to [plaid/quickstart](https://github.com/plaid/quickstart) at `5d4707883204fde096bf618e4862807b759e3c73`.

The commits that added these scripts are from Zu67 and QuinnG17.
