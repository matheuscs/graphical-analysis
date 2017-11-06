
from graphical_analysis.indicators_analysis.obv_analysis import plot_obv

from helpers.const import Interval
from helpers.stocks import get_stocks_symbols, get_stocks_data

intv = Interval()

stocks_data = get_stocks_data(get_stocks_symbols(), intv.DAY)
plot_obv(stocks_data, 'BBAS3')



