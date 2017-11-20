from graphics.patterns.candlesticks import candlestick_positioning
from graphics.patterns.candlesticks import is_candlestick_positive


def analyse_bullish_engulfing(stocks_data):
    """
    Bullish Engulfing definition:
        - 2 candles, first is negative, second is positive
        - second engulfs the first body, not necessarily the shadows

    Higher significance factors:
        - Size matters, bigger the second is to the first better it is
        - Number matters, bigger the previous candles engulfed better it is
        - Higher volume than previous candlestick
        - Upward movement
        - Over a support area

    Conclusion:
        - Reversal of movement
        - Buy signal
    """

    for stock_symbol, df in stocks_data.items():
        bullish_engulfs = []
        for i in range(1, len(df)):
            engulfeds = 0
            current_row = df.ix[i]
            for j in range(1, i):
                previous_row = df.ix[i - j]
                if not is_candlestick_positive(previous_row) and is_candlestick_positive(current_row):
                    pos = candlestick_positioning(previous_row, current_row)
                    if pos == 1:
                        engulfeds += 1
                    else:
                        break
                else:
                    break
            if engulfeds > 0:
                bullish_engulfs.append((df.index[i], engulfeds))

        if len(bullish_engulfs) > 0:
            print('\n--- BULLISH ENGULFS ---')
            print(stock_symbol)
            [print('Date: {}, Engulfeds: {}'.format(e[0], e[1])) for e in bullish_engulfs]

