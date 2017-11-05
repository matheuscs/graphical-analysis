
from graphical_analysis.candlesticks_analysis.gap_analysis import analyse
from helpers.const import Interval
from helpers.stocks import get_stocks_symbols, get_stocks_data

intv = Interval()

a = analyse(get_stocks_data(get_stocks_symbols(), intv.DAY))
# print(a)
