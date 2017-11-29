from graphical_analysis.candlesticks.engulfs import analyse_engulfs
from graphical_analysis.candlesticks.gap import analyse_gaps
from graphical_analysis.candlesticks.long_shadows import analyse_long_shadows
from graphical_analysis.candlesticks.three import analyse_threes
from stocks.my import read_stocks_data, update_db_from_request
from stocks.my_json import get_stocks_symbols


def update_db(period='1Y'):
    # update_db_from_request(period, get_stocks_symbols('ibov'), True)
    update_db_from_request(period, get_stocks_symbols('ibov'))
    update_db_from_request(period, get_stocks_symbols('smll'))
    update_db_from_request(period, get_stocks_symbols('others'))


if __name__ == '__main__':
    pass
    sd = read_stocks_data(20, get_stocks_symbols('ibov'))
    analyse_threes(sd)
    analyse_long_shadows(sd)
    analyse_engulfs(sd)
    analyse_gaps(sd)
    # update_db()
