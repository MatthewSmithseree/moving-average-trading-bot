# Moving Average Trading Bot - Backtesting Script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def backtest_strategy(dataframe):
    dataframe["Position"] = dataframe["Signal"].shift(1)
    dataframe["Return"] = dataframe["Close"].pct_change()
    dataframe["Strategy"] = dataframe["Return"] * dataframe["Position"]
    dataframe["Cumulative_Strategy"] = (1 + dataframe["Strategy"]).cumprod()
    dataframe["Cumulative_Return"] = (1 + dataframe["Return"]).cumprod()
    # plotting
    plt.figure(figsize = (12, 6))
    plt.plot(dataframe["Cumulative_Return"], label = "Buy & Hold")
    plt.plot(dataframe["Cumulative_Strategy"], label = "Strategy")
    plt.title("Cumulative Performance")
    plt.ylabel("Portfolio Value %")
    plt.xlabel("Time")
    plt.legend()
    plt.show()



# Max drawdown – how deep was your biggest portfolio drop?
# Sharpe ratio – how efficient is your return per unit of risk?
# Volatility – standard deviation of your returns
# Hit rate – % of trades that were profitable
# Average win vs. average loss

    