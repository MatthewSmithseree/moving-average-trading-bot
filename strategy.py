# Moving Average Trading Bot - Strategy Script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def generate_signals(dataframe):
    dataframe["SMA_50"] = dataframe['Close'].rolling(window=50).mean()
    dataframe["SMA_200"] = dataframe['Close'].rolling(window=200).mean()
    dataframe["Signal"] = 0
    dataframe["Signal"] = np.where(dataframe["SMA_50"] > dataframe["SMA_200"], 1, 
                            np.where(dataframe["SMA_50"] < dataframe["SMA_200"], -1, 0))
    dataframe.loc[dataframe["SMA_200"].isna(), "Signal"] = 0
    dataframe.loc[dataframe["SMA_50"].isna(), "Signal"] = 0