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
    #sharpe ratio
    avg_risk_free = 0.04396 / 252 #10 year treasury t bill
    daily_volatility = dataframe["Strategy"].std()
    avg_return = dataframe["Strategy"].mean()
    sharpe_ratio_annualized = np.sqrt(252) * ((avg_return - avg_risk_free)/daily_volatility)
    #max drawdown
    rolling_max = dataframe["Cumulative_Strategy"].cummax()
    dataframe["Drawdown"] = (dataframe["Cumulative_Strategy"] - rolling_max) / rolling_max
    max_drawdown = dataframe["Drawdown"].min() * -1
    
    # plotting
    plt.figure(figsize = (12, 6))
    plt.plot(dataframe["Cumulative_Return"], label = "Buy & Hold")
    plt.plot(dataframe["Cumulative_Strategy"], label = "Strategy")
    plt.title("Cumulative Performance")
    plt.ylabel("Portfolio Value %")
    plt.xlabel("Time")
    plt.text(
        0.90,                # X position (from 0 to 1)
        0.95,                # Y position (from 0 to 1)
        f'Sharpe: {sharpe_ratio_annualized:.2f}',
        ha='right',          # horizontal alignment
        transform=plt.gca().transAxes,
        fontsize=10
    )
    plt.text(
        0.90,
        0.90,
        f'Std: {daily_volatility:.5f}',
        ha='right',
        transform=plt.gca().transAxes,
        fontsize=10
    )
    plt.text(
        0.90,
        0.85,
        f'Max Drawdown: {max_drawdown:.3f}%',
        ha='right',
        transform=plt.gca().transAxes,
        fontsize=10
    )
    plt.legend()
    plt.show()
    return dataframe


# Max drawdown – how deep was your biggest portfolio drop?
# Sharpe ratio – how efficient is your return per unit of risk?
# Volatility – standard deviation of your returns
# Hit rate – % of trades that were profitable
# Average win vs. average loss

    