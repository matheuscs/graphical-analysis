from analysis.candlesticks.gap import analyse_gaps
from analysis.indicators.rsi import analyse_rsi
from analysis.indicators.volume import analyse_volume
from stocks.my import read_stocks_data, update_db_from_request
from stocks.my_json import get_stocks_symbols


def update_db(period='1Y'):
    update_db_from_request(period, get_stocks_symbols('ibov'), True)
    # update_db_from_request(period, get_stocks_symbols('ibov'))
    update_db_from_request(period, get_stocks_symbols('smll'))
    update_db_from_request(period, get_stocks_symbols('others'))


if __name__ == '__main__':
    pass
    # update_db()
    sd = read_stocks_data(90, get_stocks_symbols('my2'))
    # analyse_rsi(sd, overbought=200, oversold=25)
    # sd = read_stocks_data(90, get_stocks_symbols('smll'))
    # analyse_rsi(sd, overbought=200, oversold=25)
    # sd = read_stocks_data(90, get_stocks_symbols('others'))
    # analyse_rsi(sd, overbought=200, oversold=25)
    # analyse_volume(sd)
    # analyse_threes(sd)
    # analyse_long_shadows(sd)
    # analyse_engulfs(sd)
    analyse_gaps(sd)
