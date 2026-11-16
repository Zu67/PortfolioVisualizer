# PortfolioVisualizer

Python scripts for positions built from a brokerage export and for prices from Yahoo Finance. The exports themselves are not in this repository.

| Script | What it does |
| --- | --- |
| `scripts/Data Generator.py` | Uses Faker to write 100 synthetic buy and sell rows to a local `transactiondata.csv`. |
| `scripts/portfolio_calculation_quinn.py` | Reads a Robinhood activity CSV from a local path, then computes holding cost, quantity, and average price and downloads adjusted closes with yfinance. |
| `scripts/robinhood_portfolio_manipulation.py` | Same kind of holding-cost rollup from `robinhood_data.csv` in the working directory. |
| `scripts/schwab_portfolio_manipulation.py` | Same rollup for Buy and Sell rows in a local `Roth_IRA.csv`. |
| `scripts/PortfolioVisualizerInGit.py` | Downloads about 300 days of VTI and SPY. |
| `scripts/PortfolioData` | Plots cumulative returns from a local `PortfolioData.csv`. |
| `scripts/plaid_quickstart.py` | Notes for running the public Plaid quickstart. It does not contain API keys. |

`data/ETF Constituent Data - Examples.csv` is example ETF constituent data.

`quickstart` is a gitlink to [plaid/quickstart](https://github.com/plaid/quickstart) at `5d4707883204fde096bf618e4862807b759e3c73`.

The commits on this repository are from Zu67, QuinnG17, and the author recorded as `=`.
