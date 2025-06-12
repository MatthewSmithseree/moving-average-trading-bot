# Moving Average Trading Bot - Data Ingestion Script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def fetch_stock_data(ticker, startdate, enddate):
    dataframe = yf.download(ticker, start = startdate, end = enddate)
    return dataframe

msftdata = fetch_stock_data("MSFT", "2023-01-01", "2024-12-31")
print(msftdata.head())
msftdata.to_csv("MSFT_2023-to-2024")

