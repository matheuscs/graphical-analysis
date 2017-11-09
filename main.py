
from graphical_analysis.indicators.rsi import plot_rsi

from helpers.const import Interval
from helpers.stocks import get_stocks_symbols, get_stocks_data

intv = Interval()

stocks_data = get_stocks_data(get_stocks_symbols(), intv.DAY, "6M")
plot_rsi(stocks_data, 'MGLU3')


