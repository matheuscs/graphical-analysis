
from graphical_analysis.candlesticks_analysis.gap_analysis import analyse_gap
from graphical_analysis.indicators_analysis.ifr_analysis import analyse_ifr

from helpers.const import Interval
from helpers.stocks import get_stocks_symbols, get_stocks_data

intv = Interval()

stocks_data = get_stocks_data(get_stocks_symbols(), intv.DAY)
analyse_ifr(stocks_data)



