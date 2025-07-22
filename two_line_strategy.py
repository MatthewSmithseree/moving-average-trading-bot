# Moving Average Trading Bot - Strategy Script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def generate_signals(dataframe):
    dataframe["EMA_12"] = dataframe['Close'].ewm(span = 12).mean()
    dataframe["EMA_26"] = dataframe['Close'].ewm(span = 26).mean()
    dataframe["EMA_200"] = dataframe['Close'].ewm(span = 200).mean()

    dataframe["Signal"] = 0

    long_condition = (
        (dataframe["EMA_12"] > dataframe["EMA_26"]) & (dataframe["Close"] > dataframe["EMA_200"])
    )

    short_condition = (
        (dataframe["EMA_12"] < dataframe["EMA_26"]) & (dataframe["Close"] < dataframe["EMA_200"])
    )

    dataframe.loc[long_condition, "Signal"] = 1 
    dataframe.loc[short_condition, "Signal"] = -1

    dataframe.loc[dataframe["EMA_12"].isna(), "Signal"] = 0
    dataframe.loc[dataframe["EMA_26"].isna(), "Signal"] = 0
    dataframe.loc[dataframe["EMA_200"].isna(), "Signal"] = 0

    return dataframe