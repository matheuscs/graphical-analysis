from graphical_analysis.candlesticks.long_shadows import analyse_long_shadows
from stocks.my import read_stocks_data, update_db_from_request, \
    request_stocks_data
from stocks.my_json import get_stocks_symbols

if __name__ == '__main__':
    pass
    # update_db_from_request('3Y', get_stocks_symbols('my2'))
    analyse_long_shadows(read_stocks_data(60, get_stocks_symbols('my2')))
    # print(read_stocks_data(10, get_stocks_symbols('my2')))
