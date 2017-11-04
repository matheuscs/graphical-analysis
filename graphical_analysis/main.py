
from helpers.stocks import get_stocks_symbols, get_stocks_data
from patterns_analysis.gap_analysis import analyse
from helpers.const import Interval

intv = Interval()

a = analyse(get_stocks_data(get_stocks_symbols(), intv.DAY))
# print(a)
