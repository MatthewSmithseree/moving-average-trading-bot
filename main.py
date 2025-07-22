from data_ingestion import fetch_stock_data
from two_line_strategy import generate_signals
from backtesting import backtest_strategy

tests = [
    {"ticker": "AAPL", "start": "2019-01-01", "end": "2021-12-31"},
    {"ticker": "TSLA", "start": "2020-01-01", "end": "2022-12-31"},
    {"ticker": "SPY", "start": "2022-01-01", "end": "2023-12-31"},
]

results = []

for test in tests:
    ticker, start, end = test["ticker"], test["start"], test["end"]
    print(f"We're testing {ticker} from {start} to {end}")

    data = fetch_stock_data(ticker, start, end)
    data = generate_signals(data)
    data = backtest_strategy(data)

    results.append({
        "Ticker": ticker,
        "Start": start,
        "End": end
    })

print(results)
