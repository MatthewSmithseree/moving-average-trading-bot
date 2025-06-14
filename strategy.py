# Moving Average Trading Bot - Strategy Script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def generate_signals(dataframe):
    dataframe["SMA_9"] = dataframe['Close'].rolling(window=9).mean()
    dataframe["SMA_21"] = dataframe['Close'].rolling(window=21).mean()
    dataframe["SMA_55"] = dataframe['Close'].rolling(window=55).mean()

    dataframe["Signal"] = 0

    buy_signal = (
        (
            (dataframe["SMA_9"] > dataframe["SMA_21"]) | (dataframe["SMA_21"] > dataframe["SMA_55"])
        )
        & 
        (dataframe["Close"] > dataframe["SMA_9"])
    )
    
    sell_signal = (
        (
            (dataframe["SMA_9"] < dataframe["SMA_21"]) | (dataframe["SMA_21"] < dataframe["SMA_55"])
        )
        & 
        (dataframe["Close"] < dataframe["SMA_9"])
    )

    dataframe.loc[buy_signal, "Signal"] = 1
    dataframe.loc[sell_signal, "Signal"] = -1

    dataframe.loc[dataframe["SMA_9"].isna(), "Signal"] = 0
    dataframe.loc[dataframe["SMA_21"].isna(), "Signal"] = 0
    dataframe.loc[dataframe["SMA_55"].isna(), "Signal"] = 0

    return dataframe

# If (EMA(9) > EMA(21) OR EMA(21) > EMA(55)) AND Price > EMA(9):
#     Buy
# Elif (EMA(9) < EMA(21) OR EMA(21) < EMA(55)) AND Price < EMA(9):
#     Sell
# Else:
#     Hold
