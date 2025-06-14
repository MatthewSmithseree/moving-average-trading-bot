from data_ingestion import fetch_stock_data
from strategy import generate_signals
from backtesting import backtest_strategy


msftdata = fetch_stock_data("MSFT", "2024-01-01", "2024-12-31")
msftdata = generate_signals(msftdata)
msftdata = backtest_strategy(msftdata)
