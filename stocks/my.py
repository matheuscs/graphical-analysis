from stocks.my_db import read
from stocks.my_json import get_stocks_symbols
from stocks.my_request import get_price_data


def read_stocks_data(symbols=get_stocks_symbols()):
    """
    Retrieve stock data from DB

    :param period: period to be retrieved
    :param symbols: stocks symbols
    :return:
    """
    stocks_data = {}
    for symbol in symbols:
        stocks_data[symbol] = read(symbol)
    return stocks_data


def request_stocks_data(period, symbols):
    """
    Retrieve stock data from API

    :param period: period to be retrieved
    :param symbols: stocks symbols
    :return:
    """
    stocks_data = {}
    for s in symbols:
        param = {
            'q': s,
            'i': 86400,
            'p': period
        }
        stocks_data[s] = get_price_data(param)

    return stocks_data


def update_db_from_request(period='5Y',  symbols=get_stocks_symbols()):
    print(request_stocks_data(period, symbols))


