# Moving Average Trading Bot - Data Ingestion Script
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def fetch_stock_data(ticker, startdate, enddate):
    dataframe = yf.download(ticker, start = startdate, end = enddate)
    return dataframe