import json


def get_stocks_symbols():
    """
    Retrieve all stocks symbols from the json

    :return: all stocks symbols
    """
    with open(r'./data/stocks.json') as data_file:
        return json.load(data_file)['symbols']
