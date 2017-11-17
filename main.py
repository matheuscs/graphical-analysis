from graphical_analysis.candlesticks.long_shadows import analyse_long_shadows

from helpers.const import Interval
from helpers.stocks import get_stocks_symbols, get_stocks_data

intv = Interval()

stocks_data = get_stocks_data(get_stocks_symbols(), intv.DAY, "2M")
analyse_long_shadows(stocks_data)
