from graphical_analysis.candlesticks.bullish_engulfing import \
    analyse_bullish_engulfing
from helpers.const import Interval
from helpers.stocks import get_stocks_symbols, get_stocks_data

intv = Interval()

stocks_data = get_stocks_data(get_stocks_symbols(), intv.DAY, "2M")
analyse_bullish_engulfing(stocks_data)
