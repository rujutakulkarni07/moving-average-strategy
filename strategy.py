import matplotlib.pyplot as plt
import yfinance as yf


# Download historical stock data.
ticker = "AAPL"  # Example: "TCS.NS" for an Indian stock.
data = yf.download(ticker, start="2023-01-01", end="2026-01-01")

if data.empty:
    raise ValueError(f"No historical data returned for {ticker!r}.")

# Calculate two moving averages.
data["MA20"] = data["Close"].rolling(window=20).mean()
data["MA50"] = data["Close"].rolling(window=50).mean()

# Be invested when the short moving average is above the long moving average.
data["Signal"] = (data["MA20"] > data["MA50"]).astype(int)

# Backtest, shifting the signal to avoid using information from the same day.
data["DailyReturn"] = data["Close"].pct_change()
data["StrategyReturn"] = data["DailyReturn"] * data["Signal"].shift(1)
data["CumulativeMarket"] = (1 + data["DailyReturn"].fillna(0)).cumprod()
data["CumulativeStrategy"] = (1 + data["StrategyReturn"].fillna(0)).cumprod()

# Plot cumulative growth.
plt.figure(figsize=(12, 6))
plt.plot(data.index, data["CumulativeMarket"], label="Buy & Hold")
plt.plot(data.index, data["CumulativeStrategy"], label="MA Crossover Strategy")
plt.title(f"{ticker}: Strategy vs Buy & Hold")
plt.xlabel("Date")
plt.ylabel("Growth of $1")
plt.legend()
plt.tight_layout()
plt.show()

print("Final Buy & Hold return:", data["CumulativeMarket"].iloc[-1])
print("Final Strategy return:", data["CumulativeStrategy"].iloc[-1])
