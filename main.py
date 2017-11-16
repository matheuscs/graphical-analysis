from graphical_analysis.candlesticks.gap import analyse_gaps
from graphical_analysis.candlesticks.hammer import analyse_hammers

from helpers.const import Interval
from helpers.stocks import get_stocks_symbols, get_stocks_data

intv = Interval()

stocks_data = get_stocks_data(get_stocks_symbols(), intv.DAY, "4M")
print(stocks_data)
analyse_gaps(stocks_data)
analyse_hammers(stocks_data)
# print(stocks_data)
