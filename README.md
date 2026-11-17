# PortfolioVisualizer

Python scripts for positions built from a brokerage export and for prices from Yahoo Finance. The exports themselves are not in this repository.

| Script | What it does |
| --- | --- |
| `scripts/Data Generator.py` | Uses Faker to write 100 synthetic buy and sell rows to a local `transactiondata.csv`. |
| `scripts/portfolio_calculation_quinn.py` | Reads `robinhood_data.csv`. Holding cost is the amount times -1, quantity flips sign when that cost is negative, and average price is the running cost divided by the running quantity. It downloads adjusted closes for the activity-date range and prints the ITOT rows with market value and gain/loss. |
| `scripts/robinhood_portfolio_manipulation.py` | Reads the same file, expands every calendar day between the first and last activity for every symbol, and forward-fills quantity and average price. After joining adjusted closes, total cost is quantity times average price. It prints the last 25 rows. |
| `scripts/schwab_portfolio_manipulation.py` | Reads `Roth_IRA.csv`, keeps Buy and Sell rows, and does that same calendar expansion and forward-fill by symbol. It prints the tail and does not download prices. |
| `scripts/PortfolioVisualizerInGit.py` | Prints two downloads of about 300 days of VTI and SPY, then stops. See below. |
| `scripts/PortfolioData` | Reads a local `PortfolioData.csv` and plots the running sum of daily percent changes. The chart title is "Portfolio Performance". |
| `scripts/plaid_quickstart.py` | Notes for running the public Plaid quickstart. It does not contain API keys. |

`scripts/PortfolioVisualizerInGit.py` prints two downloads of about 300 days of VTI and SPY. The next loop reads `df`, which this file has not assigned, so running it from the top stops there. The lines after that are not reached. They expect `df` to be a constituents table, build Morningstar-style super-sector, sector, and industry lookup tables, and plot sector and super-sector weights. Those pie charts select `2024-03-26` and the titles say `2023-03-26`. The last cells use `df_security`, `df_benchmark`, `selected_symbol`, and `selected_benchmark`, which are also not defined here. They compute a beta, a 30-day rolling Sharpe ratio, Treynor ratio, and Jensen's alpha with a 5% risk-free rate, and plot cumulative percent price change.

`data/ETF Constituent Data - Examples.csv` is example ETF constituent data.

`quickstart` is a gitlink to [plaid/quickstart](https://github.com/plaid/quickstart) at `5d4707883204fde096bf618e4862807b759e3c73`.

The commits that added these scripts are from Zu67 and QuinnG17.
