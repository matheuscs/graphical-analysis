import json

from googlefinance.client import get_price_data


def get_stocks_symbols():
    """

    :return: all stocks symbols in the json
    """
    with open(r'..\data\stocks.json') as data_file:
        return json.load(data_file)['symbols']


def get_stocks_data(symbols, interval):
    """

    :param symbols: stocks symbols
    :param interval: interval
    :return:
    """
    stocks_data = {}
    for s in symbols:
        param = {
            'q': s,
            'i': interval,
        }
        stocks_data[s] = get_price_data(param)

    return stocks_data
