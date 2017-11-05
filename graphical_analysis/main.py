
from graphical_analysis.candlesticks_analysis.gap_analysis import analyse
from graphical_analysis.indicators.ifr import find_ifr
from helpers.const import Interval
from helpers.stocks import get_stocks_symbols, get_stocks_data

intv = Interval()

stocks_data = get_stocks_data(get_stocks_symbols(), intv.DAY)

# a = analyse(stocks_data)
# print(a)

print(find_ifr(stocks_data))
