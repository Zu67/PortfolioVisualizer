# PortfolioVisualizer

This branch is `DevelopmentPortfolioVisualizer`. The commits that added the scripts run from 2024-04-30 ("Initial commit") through 2024-05-13 ("Updating PortfolioVisualizer"). Later commits moved those files into `scripts/` and updated this README.

| File | What it does |
| --- | --- |
| `scripts/Data Generator.py` | Uses Faker to write 100 rows to a local `transactiondata.csv`. Each row is a date, a four-letter symbol, buy or sell, a fake person's name in the broker column, a quantity from 1 to 100, and a price from 10.00 to 500.00. |
| `scripts/PortfolioData` | Reads a local `PortfolioData.csv` and plots the running sum of daily percent changes. The chart title is "Portfolio Performance". |
| `scripts/PortfolioVisualizerInGit.py` | Prints two downloads of about 300 days of VTI and SPY, then stops. See below. |

`scripts/PortfolioVisualizerInGit.py` prints two downloads of about 300 days of VTI and SPY. The next loop reads `df`, which this file has not assigned, so running it from the top stops there. The lines after that are not reached. They expect `df` to be a constituents table, build Morningstar-style super-sector, sector, and industry lookup tables, and plot sector and super-sector weights. Those pie charts select `2024-03-26` and the titles say `2023-03-26`. The last cells use `df_security`, `df_benchmark`, `selected_symbol`, and `selected_benchmark`, which are also not defined here. They compute a beta, a 30-day rolling Sharpe ratio, Treynor ratio, and Jensen's alpha with a 5% risk-free rate, and plot cumulative percent price change.

The default branch, `main`, also has the holding-cost scripts and `data/ETF Constituent Data - Examples.csv`.
