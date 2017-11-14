from graphical_analysis.candlesticks.hammer import analyse_hammers
from graphical_analysis.candlesticks.shooting_star import analyse_shooting_stars
from graphical_analysis.candlesticks.hanging_man import analyse_hanging_mans
from graphical_analysis.candlesticks.inverted_hammer import analyse_inverted_hammers

from helpers.const import Interval
from helpers.stocks import get_stocks_symbols, get_stocks_data

intv = Interval()

stocks_data = get_stocks_data(get_stocks_symbols(), intv.DAY, "1Y")
analyse_hammers(stocks_data)
analyse_shooting_stars(stocks_data)
analyse_hanging_mans(stocks_data)
analyse_inverted_hammers(stocks_data)

