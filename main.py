from data_ingestion import fetch_stock_data
from three_line_strategy import generate_signals
from backtesting import backtest_strategy


data = fetch_stock_data("TSLA", "2018-01-01", "2024-12-31")
data = generate_signals(data)
data = backtest_strategy(data)
