import json
import requests
import pandas as pd

from datetime import datetime


def get_stocks_symbols():
    """
    Retrieve all stocks symbols from the json

    :return: all stocks symbols
    """
    with open(r'.\data\stocks.json') as data_file:
        return json.load(data_file)['symbols']


def get_stocks_data(symbols, interval, period="1Y"):
    """
    Retrieve stock data from API

    :param symbols: stocks symbols
    :param interval: interval
    :param period: period to be retrieved
    :return:
    """
    stocks_data = {}
    for s in symbols:
        param = {
            'q': s,
            'i': interval,
            'p': period
        }
        stocks_data[s] = get_price_data(param)

    return stocks_data


def get_price_data(query):
    r = requests.get("https://www.google.com/finance/getprices", params=query)
    lines = r.text.splitlines()
    data = []
    index = []
    basetime = 0
    for price in lines:
        cols = price.split(",")
        if cols[0][0] == 'a':
            basetime = int(cols[0][1:])
            index.append(datetime.fromtimestamp(basetime).strftime('%Y-%m-%d'))
            data.append(
                [float(cols[4]), float(cols[2]), float(cols[3]), float(cols[1]),
                 int(cols[5])])
        elif cols[0][0].isdigit():
            date = basetime + (int(cols[0]) * int(query['i']))
            index.append(datetime.fromtimestamp(date).strftime('%Y-%m-%d'))
            data.append(
                [float(cols[4]), float(cols[2]), float(cols[3]), float(cols[1]),
                 int(cols[5])])
    return pd.DataFrame(data, index=index,
                        columns=['Open', 'High', 'Low', 'Close', 'Volume'])
