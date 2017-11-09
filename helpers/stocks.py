import json

from googlefinance.client import get_price_data


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
