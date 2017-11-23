import json


def get_stocks_symbols(stock_list='my'):
    """
    Retrieve all stocks symbols from the json

    :type stock_list: object
    :return: all stocks symbols
    """
    with open(r'./data/stocks.json') as data_file:
        return json.load(data_file)[stock_list]
