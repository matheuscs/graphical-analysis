from graphical_analysis.candlesticks.engulfs import analyse_engulfs
from helpers.const import Interval
from helpers.stocks import get_stocks_symbols, get_stocks_data

intv = Interval()

stocks_data = get_stocks_data(get_stocks_symbols(), intv.DAY, "2M")
analyse_engulfs(stocks_data)
