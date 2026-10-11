
# Moving Average Crossover Strategy

A simple algorithmic trading strategy built in Python that backtests a 20-day/50-day moving average crossover against a buy-and-hold baseline, using historical stock data.

## What it does

- Downloads historical price data using yfinance
- Calculates 20-day and 50-day moving averages
- Generates a buy/sell signal: invested when the short MA is above the long MA, in cash otherwise
- Backtests the strategy's cumulative returns against simply holding the stock
- Plots both results for comparison

## Results (AAPL, 2023-2026)

- Buy and Hold: grew $1 to about $2.21
- Strategy: grew $1 to about $1.52

The strategy underperformed buy-and-hold over this period, a common finding for simple MA crossovers in strong trending markets, since they lag behind the start of rallies.

## How to run it

1. Install dependencies: pip install -r requirements.txt
2. Run the script: python strategy.py

## What I learned

My first project applying Python to a trading strategy. Covers data handling with pandas, backtesting logic, and visualizing results with matplotlib.
