from graphical_analysis.candlesticks.long_shadows import analyse_long_shadows
from graphical_analysis.candlesticks.three import analyse_threes
from stocks.my import read_stocks_data, update_db_from_request, \
    request_stocks_data
from stocks.my_json import get_stocks_symbols


def update_db(period='2Y'):
    # update_db_from_request(period, get_stocks_symbols('ibov'), True)
    update_db_from_request(period, get_stocks_symbols('ibov'))
    update_db_from_request(period, get_stocks_symbols('small'))
    update_db_from_request(period, get_stocks_symbols('others'))


if __name__ == '__main__':
    pass
    analyse_threes(read_stocks_data(60, get_stocks_symbols('ibov')))

