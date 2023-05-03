import yfinance as yf
import pandas as pd
import datetime
import time
import schedule

def get_best_stocks():
    # Define the pool of stocks for swing trading
    stock_list = = [
    "AMGN",
    "AAPL",
    "AMAT",
    "INTC",
    "PCAR",
    "PAYX",
    "MSFT",
    "ADBE",
    "CSCO",
    "XLNX",
    "QCOM",
    "COST",
    "SBUX",
    "FISV",
    "CTXS",
    "INTU",
    "AMZN",
    "EBAY",
    "BIIB",
    "CHKP",
    "GILD",
    "NLOK",
    "CMCSA",
    "FAST",
    "ADSK",
    "CTSH",
    "NVDA",
    "GOOGL",
    "ISRG",
    "VRTX",
    "HSIC",
    "BIDU",
    "ATVI",
    "ADP",
    "ROST",
    "ORLY",
    "CERN",
    "BKNG",
    "MYL",
    "MU",
    "DLTR",
    "ALXN",
    "SIRI",
    "MNST",
    "AVGO",
    "TXN",
    "MDLZ",
    "FB",
    "ADI",
    "WDC",
    "REGN",
    "LBTYK",
    "VRSK",
    "NFLX",
    "TSLA",
    "CHTR",
    "MAR",
    "ILMN",
    "LRCX",
    "EA",
    "AAL",
    "WBA",
    "KHC",
    "BMRN",
    "JD",
    "SWKS",
    "INCY",
    "PYPL",
    "CDW",
    "FOXA",
    "MXIM",
    "TMUS",
    "EXPE",
    "TCOM",
    "ULTA",
    "CSX",
    "NTES",
    "MCHP",
    "CTAS",
    "KLAC",
    "HAS",
    "JBHT",
    "IDXX",
    "WYNN",
    "MELI",
    "ALGN",
    "CDNS",
    "WDAY",
    "SNPS",
    "ASML",
    "TTWO",
    "PEP",
    "NXPI",
    "XEL",
    "AMD",
    "NTAP",
    "VRSN",
    "LULU",
    "WLTW",
    "UAL",
]

    # Define the indicators to screen stocks
    indicators = {
        'previous_close': [],
        'MovingAverage_10': [],
        'RSI_14': [],
        'volume': []
    }

    # Add your own calculations for the above indicators here
    # For example, use yfinance to get historical data for each stock and calculate the indicators

    # Add dummy data for demonstration purposes
    for stock in stock_list:
        indicators['previous_close'].append(stock + '_previous_close')
        indicators['MovingAverage_10'].append(stock + '_MOV10')
        indicators['RSI_14'].append(stock + '_RSI14')
        indicators['volume'].append(stock + '_volume')

    return pd.DataFrame(indicators, index=stock_list)

def rescreen_stocks():
    print("Re-screening stocks...")
    best_stocks = get_best_stocks()
    print(best_stocks)
