from stocks.my_db import read, delete_all, bulk_create
from stocks.my_json import get_stocks_symbols
from stocks.my_request import get_price_data


def read_stocks_data(symbols=get_stocks_symbols()):
    """
    Retrieve stock data from DB

    :param symbols: stocks symbols
    :return:
    """
    stocks_data = {}
    for symbol in symbols:
        data = read(symbol)
        if len(data):
            stocks_data[symbol] = data
    return stocks_data


def request_stocks_data(period='2Y', symbols=get_stocks_symbols()):
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


def update_db_from_request(period='2Y', reset=False,
                           symbols=get_stocks_symbols()):
    if reset:
        delete_all()
    stocks_data = request_stocks_data(period, symbols)
    data = []
    for stock, df in stocks_data.items():
        for index, row in df.iterrows():
            data.append((stock, index, row[0], row[1], row[2], row[3], row[4]))
    bulk_create(data)
