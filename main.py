from data_ingestion import fetch_stock_data
from three_line_strategy import generate_signals
from backtesting import backtest_strategy


msftdata = fetch_stock_data("MSFT", "2018-01-01", "2024-12-31")
msftdata = generate_signals(msftdata)
msftdata = backtest_strategy(msftdata)
